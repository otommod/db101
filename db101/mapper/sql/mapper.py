import os.path

from ...helpers import readfile
from ...models import NamedTable
from ...models.model import Model
from .driver import PostgresDriver
from .querybuilder import QueryBuilder


class SQLTable:
    @classmethod
    def _prefix_dict(cls, dictionary, prefix):
        return {prefix + f: v for f, v in dictionary.items()}

    def __init__(self, execute, name, keyfields):
        self._execute = execute
        self.builder = QueryBuilder(name, keyfields)

    def get(self, fields, order_by="", descending=False):
        q = self.builder.select(*fields,
                                order_by=order_by,
                                descending=descending)
        return self._execute(q)

    def set(self, key, updates):
        q = self.builder.update(*updates.keys())
        return self._execute(q, {
            **self._prefix_dict(key, "key_"),
            **self._prefix_dict(updates, "new_")
        })

    def append(self, values):
        q = self.builder.insert(*values.keys())
        return self._execute(q, [tuple(values.values())])

    def delete(self, key):
        q = self.builder.delete()
        return self._execute(q, self._prefix_dict(key, "key_"))


class SQLQuery:
    ESCAPE_CHAR = "="

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
        # assert all(k in self.arguments for k in given_params)

        params = {k: None for k in self.arguments}
        params.update(given_params)

        if hasattr(self, "ESCAPE"):
            params.update({k: self._escape(v)
                           for k, v in params.items() if k in self.escape})

        print("SQLQuery.prepare", params)
        return params


class SQLSearchQuery(SQLQuery):
    def prepare(self, given_params):
        params = super().prepare(given_params)
        params.update({"include_" + k: (k in given_params)
                       for k in self.arguments})
        return params


class QueryResult:
    def __init__(self, execute, query, params=None):
        self._execute = execute
        self._query = query
        self._params = query.prepare(params)

    def get(self, fields):
        return self._execute(self._query.query, self._params)


class SQLMapper:
    def __init__(self, conn):
        self.conn = conn
        self.driver = PostgresDriver(conn)
        self._mappings = {}

    def create_model(self, name, desc):
        model = Model.from_desc(name, desc)
        for n, q in desc.items():
            query_name = os.path.basename(os.path.splitext(n)[0])
            if "__type__" in q and q["__type__"] == "search":
                qcls = type(SQLSearchQuery)(query_name,
                                            (SQLSearchQuery,),
                                            q.copy())
            else:
                qcls = type(SQLQuery)(query_name, (SQLQuery,), q.copy())
            qcls.query = readfile(n)
            self._mappings[model._queries[query_name]] = qcls
        return model

    def __call__(self, model, *args):
        if isinstance(model, NamedTable):
            return SQLTable(self.driver.execute, *args)

        for mq, sq in self._mappings.items():
            if isinstance(model, mq):
                return QueryResult(self.driver.execute,
                                   sq(),
                                   *args)

        raise ValueError("Unkown model type %s" % str(type(model)))
