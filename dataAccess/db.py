import sqlite3 as dbapi

conn = dbapi.connect('fmf.sqlite')
conn.execute("PRAGMA foreign_keys=ON")

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

# --- Auto-discover and import all model modules so Table subclasses register ---
_models_loaded = False

def _load_all_models() -> None:
    """
    Import all modules in dataAccess.models so any Table subclasses get registered
    into Table.TABLES via Table.__init_subclass__.
    """
    global _models_loaded
    if _models_loaded:
        return

    import importlib
    import pkgutil
    import dataAccess.models as models_pkg

    for mod in pkgutil.iter_modules(models_pkg.__path__, models_pkg.__name__ + "."):
        importlib.import_module(mod.name)

    _models_loaded = True


"""
For csv files
"""

def create_tables(cur=None):
    tables = sorted(Table.TABLES, key=lambda t: t.import_order)

    with Cursor(cur) as cur:
        print("List of tables to create: ", tables)
        for t in tables:
            t.create_table(cur=cur)


def delete_tables(cur=None):
    tables = sorted(
        Table.TABLES,
        key=lambda t: t.import_order,
        reverse=True
    )

    with Cursor(cur) as cur:
        for t in tables:
            t.delete_table(cur=cur)


def import_data(cur=None):
    tables = sorted(Table.TABLES, key=lambda t: t.import_order)

    with Cursor(cur) as cur:
        for t in tables:
            t.import_data(cur=cur)


def initialize_db(wipeout=False, data_import=False, cur=None):
    print("Initializing database...")

    # Make sure all tables are registered before we create them
    _load_all_models()

    with Cursor(cur) as cur:
        with conn:
            if wipeout:
                delete_tables(cur=cur)
            create_tables(cur=cur)
            if data_import:
                import_data(cur=cur)

