from dataclasses import dataclass
from typing import Any

from dataAccess.db import Cursor
from dataAccess.utilities import Table


@dataclass
class AssessmentType(Table):
    """
    Assessment Type fake Enum data class.
    """
    CSV_NAME = "assessment_type.csv"

    @classmethod
    def create_table(cls, cur=None):
        """
        Create assessment type table.
        :param cur: Database cursor
        """
        print("Creating assessment_type table...")
        with Cursor(cur) as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS assessment_type
                        (
                            id        INTEGER PRIMARY KEY AUTOINCREMENT,
                            value      TEXT NOT NULL
                        );
                        """)

    @classmethod
    def delete_table(cls, cur=None):
        """
        Delete assessment_type table.
        :param cur: Database cursor.
        """
        with Cursor(cur) as cur:
            cur.execute("DROP TABLE IF EXISTS assessment_type;")

    @classmethod
    def import_data(cls, cur=None):
        """
        Import assessment type data from CSV.
        :param cur: Database cursor.
        """
        print("Importing assessment type data from CSV...")
        with Cursor(cur) as cur:
            for row in cls.read_csv_source():
                print(f"Inserting row into assessment type: {row}")
                cur.execute("""
                            INSERT INTO assessment_type (value)
                            VALUES (:value);
                            """, row)

    @classmethod
    def add_row(cls, cur=None, **data) -> int:
        print("Adding row to assessment: ", data)
        sql = """
              INSERT INTO assessment_type (value)
              VALUES (:value); \
              """
        with Cursor() as cur:  # todo: understand ali rabis Cursor(cur) al ne
            with cur.connection:  # todo: understand why this is needed here
                cur.execute(sql, data)
                return cur.lastrowid
        # return super(Subject, cls).add_row(**data)

    @classmethod
    def list_all(cls, cur=None) -> list[dict[Any, Any]]:
        """
        List all assessments types.
        :param cur: Database cursor.
        :return: List of assessments types.
        """
        print("Listing all assessments...")
        with Cursor() as cur:
            cur.execute("SELECT id, value FROM assessment_type;")
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]

