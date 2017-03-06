from collections import namedtuple
from functools import partialmethod, partial

from .observable import event
from .schema import SCHEMA


class InvalidKeyError(Exception):
    pass


class InvalidOperationError(Exception):
    pass


class Table(namedtuple("Table", "name key fields db")):
    def __new__(cls, name, key, fields, db):
        key = key if isinstance(key, (list, tuple)) else (key,)
        return super().__new__(cls, name, key, fields, db)

    @event
    def changed():
        pass

    def __getattr__(self, attr):
        if attr in ("get", "set", "append", "delete"):
            return partial(getattr(self.db, attr), self.name)
        raise AttributeError(attr)


class SQLModel:
    SCHEMA = SCHEMA

    def __init__(self, mapper_factory):
        self.mapper_factory = mapper_factory

        self._tables = {}
        for name, schema in self.SCHEMA.items():
            assert name.isidentifier()
            table = Table(name, schema["key"], schema["fields"], self)
            self._tables[name] = table
            setattr(self, name.title(), table)
        self.changed.add_observer(self._dispatch_to_table)

    @event
    def changed(table):
        pass

    def _dispatch_to_table(self, table):
        if table in self._tables:
            self._tables[table].changed()

    def _mapper_for(self, table):
        return self.mapper_factory(self._tables[table])

    def get(self, table, *fields, order_by="", descending=False):
        t = self._tables[table]
        if not fields:
            fields = t.fields
        return self._mapper_for(table).get(
            fields, order_by=order_by, descending=descending)

    def set(self, table, *key, **updates):
        t = self._tables[table]
        if not key:
            # Such a query could be made to mean "set every row to this value".
            # While it may be a legitimate thing to do, we don't support it.
            raise InvalidKeyError("No key given")
        if not updates:
            raise InvalidOperationError("You must update something")
        if len(key) == 1 and isinstance(key[0], dict):
            key = key[0]
        else:
            key = dict(zip(t.key, key))

        self._mapper_for(table).set(key, updates)

    def delete(self, table, *key):
        pass

    def append(self, table, *items):
        pass
