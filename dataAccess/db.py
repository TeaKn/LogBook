import sqlite3 as dbapi

conn = dbapi.connect('fmf.sqlite')

class Cursor:
    """
    Context manager that provides a database cursor and closes it after use.
    """
    def __init__(self, cur=None):
        """
        Initialize the Cursor context manager.
        """
        if cur is None:
            self.cur = conn.cursor()
            self.close = True
        else:
            self.cur = cur
            self.close = False

    def __enter__(self):
        """
        Enter the runtime context and return the cursor.
        """
        return self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context and close the cursor if it was created here.
        """
        if self.close:
            self.cur.close()

from dataAccess.utilities import Table

"""
For csv files
"""

def create_tables(cur=None):
    with Cursor(cur) as cur:
        print(Table.TABLES)
        for t in Table.TABLES:
            t.create_table(cur=cur)


def delete_tables(cur=None):
    with Cursor(cur) as cur:
        for t in reversed(Table.TABLES):
            t.delete_table(cur=cur)


def import_data(cur=None):
    with Cursor(cur) as cur:
        for t in Table.TABLES:
            t.import_data(cur=cur)


def initialize_db(wipeout=False, cur=None):
    with Cursor(cur) as cur:
        with conn:
            if wipeout:
                delete_tables(cur=cur)
            create_tables(cur=cur)
            #import_data(cur=cur) # todo: add later in some if statement

