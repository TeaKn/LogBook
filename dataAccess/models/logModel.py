from dataclasses import dataclass
from typing import Any

from dataAccess.db import Cursor
from dataAccess.utilities import Table


@dataclass
class Log(Table):
    """
    Log data class.
    """
    CSV_NAME = "log.csv"
    import_order = 5

    @classmethod
    def create_table(cls, cur=None):
        """
        Create log table.
        :param cur: Database cursor
        """
        print("Creating log table...")
        with Cursor(cur) as cur:
            cur.execute("""
        CREATE TABLE IF NOT EXISTS log
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            typeId INTEGER NOT NULL REFERENCES log_type(id),
            assessmentId INTEGER NOT NULL REFERENCES assessment(id) ON DELETE CASCADE,
            title TEXT,
            description TEXT,
            notes TEXT,
            createdOn DATETIME,
            trackedFrom DATETIME,
            trackedTo DATETIME
        );
        """)

    @classmethod
    def delete_table(cls, cur=None):
        """
        Delete log table.
        :param cur: Database cursor.
        """
        with Cursor(cur) as cur:
            cur.execute("DROP TABLE IF EXISTS log;")

    @classmethod
    def import_data(cls, cur=None):
        """
        Import log data from CSV.
        :param cur: Database cursor.
        """
        print("Importing log data from CSV...")
        with Cursor(cur) as cur:
            for row in cls.read_csv_source():
                print(f"Inserting row into log: {row}")
                cur.execute("""
                    INSERT INTO log (id, typeId, assessmentId, title, description, notes, createdOn, trackedFrom, trackedTo)
                    VALUES (:id, :typeId, :assessmentId, :title, :description, :notes, :createdOn, :trackedFrom, :trackedTo);
                """, row)

    @classmethod
    def add_row(cls, cur=None, **data) -> int:
        print("Adding row to log: ", data)
        sql = """
        INSERT INTO log (typeId, assessmentId, title, description, notes, createdOn, trackedFrom, trackedTo) 
        VALUES ((SELECT id FROM log_type WHERE type = :type), (SELECT id FROM assessment WHERE  id = :assessmentId), :title, :description, :notes, datetime('now', 'localtime'), :trackedFrom, :trackedTo);
        """ # todo: zakaj nekje pošiljam id tole je čist debilno (SELECT id FROM assessment WHERE  id = :assessmentId)
        with Cursor() as cur:  # todo: understand ali rabis Cursor(cur) al ne
            with cur.connection:  # todo: understand why this is needed here
                cur.execute(sql, data)
                return cur.lastrowid
        # return super(Subject, cls).add_row(**data)

    @classmethod
    def update_row(cls, cur=None, **data) -> int:
        print("Updating row in logs: ", data)
        sql = """
        UPDATE log
        SET title = :title, createdOn = :createdOn, trackedFrom = :trackedFrom, trackedTo = :trackedTo
        WHERE id = :log_id;
        """
        with Cursor(cur) as cur:
            with cur.connection:
                cur.execute(sql, data)
                return cur.lastrowid

    @classmethod
    def list_logs(cls, limit: int) -> list[dict[Any, Any]]:
        print(f"Listing last {limit} logs...")
        with Cursor() as cur:
            cur.execute("""
            SELECT 
                log.typeId,
                subject.name AS 'subjectName',
                log.createdOn,
                log.title,
                log.description
                FROM LOG log
                JOIN ASSESSMENT assessment ON log.assessmentId = assessment.id
                JOIN SUBJECT subject ON assessment.subjectId = subject.id
            ORDER BY log.createdOn DESC
            LIMIT :n;
            """, {"n": limit})
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]

    @classmethod
    def list_total_time_by_subject(cls, cur=None) -> list[dict[Any, Any]]:
        print("Listing total time by subject calculated from logs...")
        with Cursor() as cur:
            cur.execute("""
                        SELECT subject.name, 
                        SUM(strftime('%s', log.trackedTo) - strftime('%s', log.trackedFrom)) / 3600 AS hours
                        FROM LOG log
                        JOIN ASSESSMENT assessment ON log.assessmentId = assessment.id
                        JOIN SUBJECT subject ON assessment.subjectId = subject.id
                        WHERE log.typeId = 1
                        GROUP BY subject.name;
            """)
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows] # todo: daj v readme da sem tukaj uporabila strftime kokr na izpitu

    @classmethod
    def list_total_time_by_day(cls, cur=None) -> list[dict[Any, Any]]:
        print("Listing total time by subject calculated from logs...")
        with Cursor() as cur:
            cur.execute("""
                        SELECT DATE(log.trackedFrom) as date,
                               SUM(strftime('%s', log.trackedTo) - strftime('%s', log.trackedFrom)) / 3600 AS hours
                        FROM LOG log
                        WHERE log.typeId = 1
                        GROUP BY DATE(log.trackedFrom);
                        """)
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in
                    rows]  # todo: daj v readme da sem tukaj uporabila strftime kokr na izpitu

    @classmethod
    def get_last_current_log(cls) -> dict[Any, Any]:
        print("Get last current log")
        with Cursor() as cur:
            cur.execute("""
            SELECT 
                *,  
                concat(subject.name, ' : ', assessment.title) AS 'logSubject'
            FROM LOG log
                JOIN assessment ON log.assessmentId = assessment.id
                JOIN subject ON assessment.subjectId = subject.id
            ORDER BY log.trackedTo 
                DESC LIMIT 1
            """)
            row = cur.fetchone()
            col_names = tuple(d[0] for d in cur.description)
            return cls.from_row(row, col_names)

    @classmethod
    def from_row(cls, row: tuple, col_names: tuple) -> dict[Any, Any]:
        """
        Map a DB row (sequence) + column names to dictionary.
        """
        data = {name: row[idx] for idx, name in enumerate(col_names)}
        return data