"""
Represent data from db with Python objects.
# TODO: refactor so that not all busniess logic lives in this one file
"""
import sqlite3

from PersistanceLayer import db

conn = sqlite3.connect('fmf.db')
db.initial_create_db(conn)

subject, assigment = db.prepare_tables(conn)

class Subject:
    """
    Subject data class.
    """
    def __init__(self, name, id=None):
        """
        Constructor
        """
        self.id = id
        self.name = name

    def __str__(self):
        """
        String representation
        """
        return self.name

    def persist_to_db(self):
        """
        Persist subject to db
        """
        assert self.id is None
        with conn:
            self.id = subject.add_row(name = self.name)

    def list_subjects(self):
        """
        List all subjects.
        """
        sql = """
        SELECT * FROM subject;
        """
        for id, name in conn.execute(sql):
            yield (id, name)