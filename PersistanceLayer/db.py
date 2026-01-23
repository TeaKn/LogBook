import csv

PARAM_FMT = ":{}"


class Table:
    """
    Class, that represents a table in a database.

    Class fields:
    - name: table name
    - data: name of file with data or None
    """
    name = None
    data = None

    def __init__(self, conn):
        """
        Konstruktor razreda.
        """
        self.conn = conn

    def create(self):
        """
        Method for creating a table.
        Override it.
        """
        raise NotImplementedError

    def delete(self):
        """
        Method for deleting a table.
        """
        self.conn.execute(f"DROP TABLE IF EXISTS {self.name};")

    def import_table(self, encoding="UTF-8"):
        """"
        Method for importing a table.
        """
        if self.data is None:
            return
        with open(self.data, encoding=encoding) as file:
            data = csv.reader(file)
            columns = next(data)
            for row in data:
                row = {k: None if v == "" else v for k, v in zip(columns, row)}
                self.add_row(**row)

    def empty(self):
        """
        Method for emptying table.
        """
        self.conn.execute(f"DELETE FROM {self.name};")

    def add(self, columns=None):
        """
        Method for building query.

        Arguments:
            - columns: list of column names
        """
        return f"""
            INSERT INTO {self.name} ({", ".join(columns)})
            VALUES ({", ".join(PARAM_FMT.format(s) for s in columns)});
        """

    def add_row(self, **data):
        """
        Method for adding row.

        Arguments:
            - named parameters: values in columns
        """
        data = {key: value for key, value in data.items()
                if value is not None}
        query = self.add(data.keys())
        cur = self.conn.execute(query, data)
        return cur.lastrowid

class Subject(Table):
    """
    Table for FMF subject.
    """
    name = "subject"
    data = "data/subject.csv"

    def create(self):
        """
        Create table subject.
        :return:
        """
        self.conn.execute("""
        CREATE TABLE subject
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """)

    def add_row(self, **data):
        return super().add_row(**data)

def create_tables(tables):
    """
    Creates tables.
    """
    for t in tables:
        t.create()

def delete_tables(tables):
    """
    Deletes tables.
    """
    for t in tables:
        t.delete()

def import_data(tables):
    """
    Import data into tables.
    """
    for t in tables:
        t.import_table()

def empty_tables(tables):
    """
    Empty tables.
    """
    for t in tables:
        t.empty()

def prepare_tables(conn):
    """
    Prepares objects for tables.
    """
    subject = Subject(conn)
    return [subject]

def create_db(conn):
    """
    Creates database.
    """
    tables = prepare_tables(conn)
    delete_tables(tables)
    create_tables(tables)
    import_data(tables)

def initial_create_db(conn):
    """
    Creates database, if it does not exist.
    """
    with conn:
        cur = conn.execute("SELECT COUNT(*) FROM sqlite_master")
        if cur.fetchone() == (0, ):
            create_db(conn)