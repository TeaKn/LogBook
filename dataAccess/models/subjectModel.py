from dataclasses import dataclass

from dataAccess.db import Cursor
from dataAccess.utilities import Table

@dataclass
class Subject(Table):
    """
    Subject data class.
    """
    CSV_NAME = "subject.csv"

    @classmethod
    def create_table(cls, cur=None):
        """
        Create subject table.
        :param cur: Database cursor.
        """
        print('probal sem kreirat tabelo subject')
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
        print("insteral sem value v subject")
        with Cursor(cur) as cur:
            for row in cls.read_csv_source():
                print(f"Inserting row into subject: {row}")
                cur.execute("""
                    INSERT INTO subject (name)
                    VALUES (:name);
                """, row)

    @classmethod
    def add_row(cls, cur=None, **data) -> int:
        print("Insertal sem value v subject preko add_row")
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
    def list_all(cls, cur=None):
        """
        List all subjects.
        :param cur: Database cursor.
        :return: List of subjects.
        """
        print("Exectural sem list all query")
        with Cursor() as cur:
            cur.execute("SELECT id, name FROM subject;")
            return cur.fetchall()

