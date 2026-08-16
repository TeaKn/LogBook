from dataclasses import dataclass
from typing import Any

from dataAccess.db import Cursor
from dataAccess.utilities import Table


@dataclass
class LogType(Table):
    """
    Log Type fake Enum data class.
    """
    CSV_NAME = "log_type.csv"

    @classmethod
    def create_table(cls, cur=None):
        """
        Create log type table.
        :param cur: Database cursor
        """
        print("Creating log_type table...")
        with Cursor(cur) as cur:
            cur.execute("""
                        CREATE TABLE IF NOT EXISTS log_type
                        (
                            id        INTEGER PRIMARY KEY AUTOINCREMENT,
                            type      TEXT NOT NULL
                        );
                        """)

    @classmethod
    def delete_table(cls, cur=None):
        """
        Delete log_type table.
        :param cur: Database cursor.
        """
        with Cursor(cur) as cur:
            cur.execute("DROP TABLE IF EXISTS log_type;")

    @classmethod
    def import_data(cls, cur=None):
        """
        Import log type data from CSV.
        :param cur: Database cursor.
        """
        print("Importing log type data from CSV...")
        with Cursor(cur) as cur:
            for row in cls.read_csv_source():
                print(f"Inserting row into log type: {row}")
                cur.execute("""
                            INSERT INTO log_type (type)
                            VALUES (:type);
                            """, row)

    @classmethod
    def add_row(cls, cur=None, **data) -> int:
        print("Adding row to log type: ", data)
        sql = """
              INSERT INTO log_type (type)
              VALUES (:type); \
              """
        with Cursor() as cur:  # todo: understand ali rabis Cursor(cur) al ne
            with cur.connection:  # todo: understand why this is needed here
                cur.execute(sql, data)
                return cur.lastrowid
        # return super(Subject, cls).add_row(**data)

    @classmethod
    def list_all(cls, cur=None) -> list[dict[Any, Any]]:
        """
        List all log types.
        :param cur: Database cursor.
        :return: List of log types.
        """
        print("Listing all log types...")
        with Cursor() as cur:
            cur.execute("SELECT id, type FROM log_type;")
            rows = cur.fetchall()
            col_names = tuple(d[0] for d in cur.description)
            return [cls.from_row(row, col_names) for row in rows]

