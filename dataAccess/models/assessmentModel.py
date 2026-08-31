from dataclasses import dataclass
from typing import Any

from dataAccess.db import Cursor
from dataAccess.utilities import Table


@dataclass
class Assessment(Table):
    """
    Assessment data class.
    """
    CSV_NAME = "assessment.csv"
    import_order = 3

    @classmethod
    def create_table(cls, cur=None):
        """
        Create assessment table.
        :param cur: Database cursor
        """
        print("Creating assessment table...")
        with Cursor(cur) as cur:
            cur.execute("""
        CREATE TABLE IF NOT EXISTS assessment
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subjectId INTEGER NOT NULL REFERENCES subject(id),
            typeId INTEGER NOT NULL REFERENCES assessment_type(id),
            title TEXT,
            createdOn DATETIME,
            dueDate DATETIME,
            doneOn DATETIME,
            grade TEXT
        );
        """)

    @classmethod
    def delete_table(cls, cur=None):
        """
        Delete assessment table.
        :param cur: Database cursor.
        """
        with Cursor(cur) as cur:
            cur.execute("DROP TABLE IF EXISTS assessment;")

    @classmethod
    def import_data(cls, cur=None):
        """
        Import assessment data from CSV.
        :param cur: Database cursor.
        """
        print("Importing assessment data from CSV...")
        with Cursor(cur) as cur:
            for row in cls.read_csv_source():
                print(f"Inserting row into assessment: {row}")
                cur.execute("""
                    INSERT INTO assessment (id, subjectId, typeId, title, createdOn, dueDate, doneOn, grade)
                    VALUES (:id, :subjectId, :typeId, :title, :createdOn, :dueDate, :doneOn, :grade);
                """, row)

    @classmethod
    def add_row(cls, cur=None, **data) -> int:
        print("Adding row to assessment: ", data)
        sql = """
        INSERT INTO assessment (subjectId, typeId, title, createdOn, dueDate, doneOn, grade)
        VALUES ((SELECT id FROM subject WHERE name = :subject), (SELECT id FROM assessment_type WHERE  value = :type), :title, datetime('now', 'localtime'), :dueDate, null, null);
        """
        with Cursor() as cur:  # todo: understand ali rabis Cursor(cur) al ne
            with cur.connection:  # todo: understand why this is needed here
                cur.execute(sql, data)
                return cur.lastrowid
        # return super(Subject, cls).add_row(**data)

    @classmethod
    def update_row(cls, cur=None, **data) -> int:
        print("Updating row in assessment: ", data)
        sql = """
        UPDATE assessment
        SET title = :title, createdOn = :createdOn, dueDate = :dueDate, doneOn = :doneOn, grade = :grade
        WHERE id = :assessment_id;
        """
        with Cursor(cur) as cur:
            with cur.connection:
                cur.execute(sql, data)
                return cur.lastrowid

    @classmethod
    def delete_row(cls, id: int):
        print("Deleting row in assessment with id: ", id)
        with Cursor() as cur:
            cur.execute("""
                        DELETE FROM assessment
                            WHERE id = ?
                        """, (id,)
                        )

    @classmethod
    def list_all(cls, cur=None) -> list[dict[Any, Any]]:
        """
        List all assessments.
        :param cur: Database cursor.
        :return: List of assessments.
        """
        print("Listing all assessments...")
        with Cursor() as cur:
            cur.execute("""
                        SELECT assessment.id, subject.name AS 'subject_name', assessment_type.value AS 'type', title, createdOn, dueDate, doneOn, grade 
                        FROM assessment
                        JOIN assessment_type ON assessment.typeId = assessment_type.id
                        JOIN subject ON assessment.subjectId = subject.id
                        ORDER BY dueDate DESC;
            """)
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]


    @classmethod
    def list_open_assessments_due_within(cls, days: int, cur=None) -> list[dict[Any, Any]]:
        """
        List all assessments that are due within the specified number of days.
        :param days: Number of days until due date.
        :param cur: Database cursor.
        :return: List of assessments.
        """
        print(f"Listing assessments due within {days} days...")
        with Cursor() as cur:
            cur.execute("""
                SELECT subject.name AS 'subject_name', assessment_type.value AS 'type', title, dueDate 
                FROM assessment 
                JOIN assessment_type ON assessment.typeId = assessment_type.id
                JOIN subject ON assessment.subjectId = subject.id
                WHERE dueDate BETWEEN date('now') AND date('now', '+' || ? || ' days') AND doneOn is null
                ORDER BY dueDate ASC;
            """, (days,))
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]

    @classmethod
    def list_assessments_count_for_subject_by_type(cls) -> list[dict[Any, Any]]:
        """
        List sum of assessments by type for subject.
        """
        print(f"Listing assessment aggregate by type...")
        with Cursor() as cur:
            cur.execute("""
                SELECT 
                    s.name AS 'subject_name',
                    SUM(CASE WHEN a.typeId = 1 THEN 1 ELSE 0 END) AS 'final_exam',
                    SUM(CASE WHEN a.typeId = 2 THEN 1 ELSE 0 END) AS 'oral_exam',
                    SUM(CASE WHEN a.typeId = 3 THEN 1 ELSE 0 END) AS 'midterm_exam',
                    SUM(CASE WHEN a.typeId = 4 THEN 1 ELSE 0 END) AS 'course_paper',
                    SUM(CASE WHEN a.typeId = 5 THEN 1 ELSE 0 END) AS 'homework',
                    SUM(CASE WHEN a.typeId = 11 THEN 1 ELSE 0 END) AS 'project',
                    SUM(CASE WHEN a.typeId = 12 THEN 1 ELSE 0 END) AS 'quiz',
                    COUNT(a.id) AS 'total'
                FROM subject s
                    LEFT JOIN assessment a ON a.subjectId = s.id
                    GROUP BY s.id
            """)
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]


    @classmethod
    def list_all_for_subject(cls, subject_name: str) -> list[dict[Any, Any]]:
        """
        List all assessments for subject with subject name.
        """
        with Cursor() as cur:
            cur.execute("""
                SELECT * FROM assessment JOIN subject s ON assessment.subjectId = s.id
                    WHERE s.name == ?
            """, (subject_name,))
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]

    @classmethod
    def from_row(cls, row: tuple, col_names: tuple) -> dict[Any, Any]:
        """
        Map a DB row (sequence) + column names to dictionary.
        """
        data = {name: row[idx] for idx, name in enumerate(col_names)}
        return data