import os.path

from .helpers import read_from


class SQLQueryMetaclass(type):
    def __new__(meta, name, bases, attrs, **kwds):
        # assert "ARGS" in attrs, name
        # assert "RETURNS" in attrs, name

        return super().__new__(meta, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        if not hasattr(cls, "ALL"):
            cls.ALL = {}

        if hasattr(cls, "QUERY_FILE"):
            basedir = getattr(cls, "BASE_DIR", ".")
            suffix = getattr(cls, "SUFFIX", "")
            cls.QUERY = read_from(
                os.path.join(basedir, cls.QUERY_FILE + suffix))

        if hasattr(cls, "QUERY"):
            cls.ALL[name] = cls

        super().__init__(name, bases, attrs)


class SQLQuery(metaclass=SQLQueryMetaclass):
    ESCAPE_CHAR = "="
    BASE_DIR = "sql"
    SUFFIX = ".pgsql"

    @classmethod
    def _escape(cls, term):
        if term is None:
            return term
        return (term.replace(cls.ESCAPE_CHAR, 2*cls.ESCAPE_CHAR)
                    .replace("%", cls.ESCAPE_CHAR + "%")
                    .replace("_", cls.ESCAPE_CHAR + "_"))

    @classmethod
    def by_name(cls, name):
        return cls.ALL_THE_QUERIES[name]()

    def prepare(self, given_params):
        assert all(k in self.ARGUMENTS for k in given_params)

        params = {k: None for k in self.ARGUMENTS}
        params.update(given_params)

        if hasattr(self, "ESCAPE"):
            params.update({k: self._escape(v)
                           for k, v in params.items() if k in self.ESCAPE})

        print("SQLQuery.prepare", params)
        return params


class SQLSearchQuery(SQLQuery):
    def prepare(self, given_params):
        params = super().prepare(given_params)
        params.update({"include_" + k: (k in given_params)
                       for k in self.ARGUMENTS})
        return params
