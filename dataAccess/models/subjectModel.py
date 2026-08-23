from dataclasses import dataclass
from typing import Any

from dataAccess.db import Cursor
from dataAccess.utilities import Table

@dataclass
class Subject(Table):
    """
    Subject data class.
    """
    CSV_NAME = "subject.csv"
    import_order = 1

    @classmethod
    def create_table(cls, cur=None):
        """
        Create subject table.
        :param cur: Database cursor.
        """
        print("Creating subject table...")
        with Cursor(cur) as cur:
            cur.execute("""
        CREATE TABLE IF NOT EXISTS subject
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """)

    @classmethod
    def delete_table(cls, cur=None):
        """
        Delete subject table.
        :param cur: Database cursor.
        """
        with Cursor(cur) as cur:
            cur.execute("DROP TABLE IF EXISTS subject;")

    @classmethod
    def import_data(cls, cur=None):
        """
        Import subject data from CSV.
        :param cur: Database cursor.
        """
        print("Importing subject data from CSV...")
        with Cursor(cur) as cur:
            for row in cls.read_csv_source():
                print(f"Inserting row into subject: {row}")
                cur.execute("""
                    INSERT INTO subject (id, name)
                    VALUES (:id, :name);
                """, row)

    @classmethod
    def add_row(cls, cur=None, **data) -> int:
        print("Adding row to subject: ", data)
        sql = """
              INSERT INTO subject (name)
              VALUES (:name);
              """
        with Cursor() as cur: # todo: understand ali rabis Cursor(cur) al ne
            with cur.connection: # todo: understand why this is needed here
                cur.execute(sql, data)
                return cur.lastrowid
        #return super(Subject, cls).add_row(**data)

    @classmethod
    def list_all(cls, cur=None) -> list[dict[Any, Any]]:
        """
        List all subjects.
        :param cur: Database cursor.
        :return: List of subjects.
        """
        print("Listing all subjects...")
        with Cursor() as cur:
            cur.execute("SELECT id, name FROM subject;")
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
