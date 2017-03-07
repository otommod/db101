from collections import namedtuple
from functools import partial

from ..observable import eventsource
from ..schema import SCHEMA
from .exceptions import InvalidKeyError, InvalidOperationError


class Table(namedtuple("Table", "name key fields db")):
    def __new__(cls, name, key, fields, db):
        key = key if isinstance(key, (list, tuple)) else (key,)
        return super().__new__(cls, name, key, fields, db)

    @eventsource
    def changed():
        pass

    def __getattr__(self, attr):
        if attr in ("get", "set", "append", "delete"):
            return partial(getattr(self.db, attr), self.name)
        raise AttributeError(attr)


class TableModel:
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

    @eventsource
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
        ok, result = self._mapper_for(table).get(fields,
                                                 order_by=order_by,
                                                 descending=descending)
        if not ok:
            raise InvalidOperationError(result)
        return result

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

        ok, changes = self._mapper_for(table).set(key, updates)
        if not ok:
            raise InvalidOperationError(changes)
        self.changed(table)

    def append(self, table, item):
        t = self._tables[table]
        if isinstance(item, (list, tuple)):
            item = dict(zip(t.fields, item))

        ok, changes = self._mapper_for(table).append(item)
        if not ok:
            raise InvalidOperationError(changes)
        self.changed(table)

    def delete(self, table, *key):
        t = self._tables[table]
        if len(key) == 1 and isinstance(key[0], dict):
            key = key[0]
        else:
            key = dict(zip(t.key, key))

        ok, changes = self._mapper_for(table).delete(key)
        if not ok:
            raise InvalidOperationError(changes)
        self.changed(table)
