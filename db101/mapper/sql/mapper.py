import os.path
from .driver import PostgresDriver
from .helpers import namedtuple_wrapper
from .querybuilder import QueryBuilder
from .queries import SQLQuery, SQLSearchQuery

from ...models import NamedTable
from ...models.model import Model
from ...helpers import readfile


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
        # result_type = self._wrapper(fields)
        data = self._execute(q)
        # return [result_type(*i) for i in data]
        return data

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


class QueryResult:
    def __init__(self, execute, query, params=None):
        self._execute = execute
        self._query = query
        self._params = query.prepare(params)

    def get(self, fields):
        return self._execute(self._query.query, self._params)


class SQLMapper:
    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.conn = conn
        self.driver = PostgresDriver(conn)
        self.result_wrapper = result_wrapper
        self._mappings = {}

    def _wrap_query(self, query, params=None):
        sqlquery = SQLQuery._registry[type(query).__name__]

        # FIXME
        query_obj = sqlquery()
        query_obj.ARGUMENTS = query.ARGUMENTS
        query_obj.RETURNS = query.RETURNS

        print("SQLMapper._wrap_query(", query, params, ")")
        return QueryResult(self.driver.execute, query_obj, params)

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
