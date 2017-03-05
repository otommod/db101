from collections import namedtuple

import psycopg2
from psycopg2.sql import SQL, Identifier

from .misc import valid_ident
from .schema import SCHEMA
from .observable import event


def namedtuple_wrapper(fields):
    assert all(valid_ident(f) for f in fields)
    return namedtuple("row", fields)


class InvalidKeyError(Exception):
    pass


class InvalidOperationError(Exception):
    pass


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


class QueryBuilder:
    def __init__(self, tablename, pk_fields):
        if not isinstance(pk_fields, (list, tuple)):
            pk_fields = [pk_fields]

        self.table = Identifier(tablename)
        self.key = SQL(" AND ").join(
            Identifier(f) + SQL(" = %%(key_%s)s" % f) for f in pk_fields)

    def select(self, *columns, order_by="", descending=False):
        ordering = Identifier(order_by)
        selection = SQL(", ").join(Identifier(c) for c in columns)

        if not order_by:
            return SQL("SELECT {0} FROM {1};").format(
                selection, self.table)
        elif descending:
            return SQL("SELECT {0} FROM {1} ORDER BY {2} DESC;").format(
                selection, self.table, ordering)
        else:
            return SQL("SELECT {0} FROM {1} ORDER BY {2};").format(
                selection, self.table, ordering)

    def insert(self, item):
        "INSERT INTO {0} ({1}) VALUES {2};"
        pass

    def update(self, *fields):
        return SQL("UPDATE {0} SET {1} WHERE {2};").format(
            self.table,
            SQL(", ").join(
                Identifier(f) + SQL(" = %%(new_%s)s" % f) for f in fields),
            self.key)

    def delete(self, key_field):
        return SQL("DELETE FROM {0} WHERE {1};").format(
            self.table, self.key)


class Table:
    def __init__(self, db, name, key, fields):
        self.name = name
        self.key = key
        self.fields = fields

        self._db = db
        self._qb = QueryBuilder(name, key)

    @event
    def changed():
        pass

    def __getattr__(self, attr):
        return getattr(self._db, attr)


class SQLModel:
    SCHEMA = SCHEMA

    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.driver = SQLDriver(conn)
        self.result_wrapper = result_wrapper

        self.tables = {}
        for name, table in self.SCHEMA.items():
            key = table["key"]
            if not isinstance(key, (list, tuple)):
                key = (key,)
            self.tables[name] = Table(self, name, key, table["fields"])

        self.changed.add_observer(self._dispatch_event)

    @event
    def changed(table):
        pass

    def _dispatch_event(self, table):
        if table in self.tables:
            self.tables[table].changed()

    def get(self, table, *fields, order_by="", descending=False):
        t = self.tables[table]
        if not fields:
            fields = t.fields
        q = t._qb.select(*fields, order_by=order_by, descending=descending)

        result_type = self.result_wrapper(fields)
        return [result_type(*i) for i in self.driver.execute(q)]

    def set(self, table, *key, **updates):
        t = self.tables[table]
        if not len(key):
            # Such a query could be made to mean "set every row to the same
            # value(s)".  While it may be a legitimate thing to do, we do not
            # support it for now.
            raise InvalidKeyError("No key given")
        if not updates:
            raise InvalidOperationError("You must update something")
        if len(key) > 1 or not isinstance(key[0], dict):
            key = dict(zip(t.key, key))
        else:
            key = key[0]

        q = t._qb.update(*updates.keys())
        print(q.as_string(self.driver.conn))

        new_fields = {"new_" + f: v for f, v in updates.items()}
        self.driver.execute(q, {**key, **new_fields})

    def delete(self, table, *key):
        pass

    def append(self, table, *items):
        pass

    # def patients_num(self):
    #     return self.driver.execute(AGGREGATE)[0][0]

    # def contracts(self):
    #     return self.driver.execute(ORDER_BY)
