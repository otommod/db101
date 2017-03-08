from .driver import PostgresDriver
from .helpers import namedtuple_wrapper
from .querybuilder import QueryBuilder


class SQLTable:
    @classmethod
    def _prefix_dict(cls, dictionary, prefix):
        return {prefix + f: v for f, v in dictionary.items()}

    def __init__(self, factory, name, keyfields):
        self._factory = factory
        self.builder = QueryBuilder(name, keyfields)

    def _wrapper(self, fields):
        return self._factory.result_wrapper(fields)

    def _execute(self, query, params=None):
        return self._factory.execute(query, params)

    def get(self, fields, order_by="", descending=False):
        q = self.builder.select(*fields,
                                order_by=order_by,
                                descending=descending)
        result_type = self._wrapper(fields)
        data = self._execute(q)
        return [result_type(*i) for i in data]

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


class TableMapper:
    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.conn = conn
        self.driver = PostgresDriver(conn)
        self.result_wrapper = result_wrapper

    def execute(self, query, params=None):
        return self.driver.execute(query, params)

    def __call__(self, *args):
        return SQLTable(self, *args)
