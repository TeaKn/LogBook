class Table:
    """
    Base class for database tables.
    Subclasses should define the CSV_SOURCE class attribute for the CSV file name.
    """
    TABLES = []

    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.TABLES.append(cls)

    @classmethod
    def create_table(cls, cur=None):
        raise NotImplementedError

    @classmethod
    def delete_table(cls, cur=None):
        raise NotImplementedError

    @classmethod
    def import_data(cls, cur=None):
        raise NotImplementedError

    @classmethod
    def add_row(cls, cur=None, **data):
        raise NotImplementedError

    @classmethod
    def read_csv_source(cls):
        """
        Read data from CSV file specified in VIR class attribute.
        Yields dictionaries mapping column names to values.
        """
        import csv
        with open(f"dataAccess/data/{cls.CSV_NAME}") as f:
            rd = csv.reader(f)
            columns = next(rd)
            for row in rd:
                yield dict(zip(columns, row))



class Entity:
    """
    Base class for entities with a NAME attribute.
    Subclasses should define the NAME class attribute for the entity name.
    """
    def __bool__(self):
        return getattr(self, self.NAME) is not None

    def __str__(self):
        print(getattr(self, self.NAME))
        return getattr(self, self.NAME) if self else f"<entity of type {self.__class__}>"

    def __init_subclass__(cls, /, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.NULL = cls()