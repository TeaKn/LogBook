"""
predstavil podatke iz baze v obliki Pythonovih objektov.
"""
import dataclasses
import sqlite3

from PersistanceLayer import db

conn = sqlite3.connect('data/subject.db')
db.initial_create_db(conn)
conn.execute('PRAGMA foreign_keys = ON')

subject = db.prepare_tables(conn)


class Subject():
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
        assert self.id is not None
        with conn:
            self.id = subject.add_row(name = self.name)