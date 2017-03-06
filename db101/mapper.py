from collections import namedtuple

import psycopg2
from psycopg2.sql import SQL, Identifier


def namedtuple_wrapper(fields):
    assert all(f.isidentifier() for f in fields)
    return namedtuple("row", fields)


class QueryBuilder:
    @classmethod
    def _idlist(cls, fields, *, join=None):
        l = (Identifier(f) for f in fields)
        return list(l) if join is None else SQL(join).join(l)

    @classmethod
    def _eqlist(cls, fields, *, prefix="", join=None):
        l = (Identifier(f) + SQL(" = %%(%s%s)s" % (prefix, f)) for f in fields)
        return list(l) if join is None else SQL(join).join(l)

    def __init__(self, table, key_fields):
        if not isinstance(key_fields, (list, tuple)):
            key_fields = [key_fields]

        self.table = Identifier(table)
        self.key_selection = self._eqlist(key_fields,
                                          prefix="key_", join=" AND ")

    def select(self, *fields, order_by="", descending=False):
        ordering = Identifier(order_by)
        selection = self._idlist(fields, join=", ")

        if not order_by:
            return SQL("SELECT {0} FROM {1};").format(
                selection, self.table)
        elif not descending:
            return SQL("SELECT {0} FROM {1} ORDER BY {2};").format(
                selection, self.table, ordering)
        else:
            return SQL("SELECT {0} FROM {1} ORDER BY {2} DESC;").format(
                selection, self.table, ordering)

    def update(self, *fields):
        return SQL("UPDATE {0} SET {1} WHERE {2};").format(
            self.table,
            self._eqlist(fields, prefix="new_", join=", "),
            self.key_selection)

    def insert(self, *fields):
        return SQL("INSERT INTO {0} ({1}) VALUES %s;").format(
            self.table, self._idlist(fields, join=", "))

    def delete(self):
        return SQL("DELETE FROM {0} WHERE {1};").format(
            self.table, self.key_selection)


class SQLDriver:
    # TODO: The first time a command is executed, a new transaction is created.
    # These need to be commited manually.  If not, the connection will sit in
    # an "idle in transaction" state, even for simple SELECTs and that's not
    # good.  Consider either autocommit mode or 'with' block on the connection
    # object.  This will not close the connection, rather, it will commit the
    # transaction.

    def __init__(self, conn):
        self.conn = conn
        self.conn.autocommit = True

    def execute(self, query, *args, **kwargs):
        with self.conn.cursor() as cur:
            cur.execute(query, *args, **kwargs)
            try:
                return cur.fetchall()
            except psycopg2.ProgrammingError:
                pass


class SQLMapperFactory:
    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.conn = conn
        self.driver = SQLDriver(conn)
        self.result_wrapper = result_wrapper

    def __call__(self, table):
        return SQLMapper(self, table)


class SQLMapper:
    @classmethod
    def _prefix_dict(cls, dictionary, prefix):
        return {prefix + f: v for f, v in dictionary.items()}

    def __init__(self, factory, tabledef):
        self.factory = factory
        self.tabledef = tabledef
        self.builder = QueryBuilder(tabledef.name, tabledef.key)

    def get(self, fields, order_by="", descending=False):
        q = self.builder.select(*fields, order_by=order_by, descending=descending)
        return self.factory.driver.execute(q)

    def set(self, key, updates):
        q = self.builder.update(*updates.keys())
        print(q.as_string(self.factory.conn))

        self.factory.driver.execute(q, {**self._prefix_dict(key, "key_"),
                                        **self._prefix_dict(updates, "new_")})

    def append(self, values):
        q = self.builder.insert(*values.keys())
        self.factory.driver.execute(q, [tuple(values.values())])

    def delete(self, key):
        q = self.builder.delete()
        self.factory.driver.execute(q, self._prefix_dict(key, "key_"))
