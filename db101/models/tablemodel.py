from collections import namedtuple
from functools import partial

from ..observable import eventsource
from ..schema import SCHEMA
from ..exceptions import InvalidKeyError, InvalidOperationError


class Table:
    mapper_factory = None

    @classmethod
    def loopup(cls, name):
        assert cls.mapper_factory

        schema = SCHEMA[name]
        return cls(name,
                   schema["key"],
                   schema["fields"],
                   cls.mapper_factory(name, schema))

    def __init__(self, mapper, name, keyfields, fields):
        self._mapper = mapper

        self.name = name
        self.fields = fields
        self.keyfields = keyfields.copy()
        if not isinstance(keyfields, (tuple, list)):
            self.keyfields = (keyfields,)

    @eventsource
    def changed():
        pass

    def get(self, *fields, order_by="", descending=False):
        if not fields:
            fields = self.fields
        return self._mapper.get(fields,
                                order_by=order_by,
                                descending=descending)

    def set(self, key, **updates):
        if not key:
            # Such a query could be made to mean "set every row to this value".
            # While it may be a legitimate thing to do, we don't support it.
            raise InvalidKeyError("No key given")
        if not updates:
            raise InvalidOperationError("You must update something")

        self._mapper.set(key, updates)
        self.changed()

    def append(self, item):
        if isinstance(item, (list, tuple)):
            item = dict(zip(t.fields, item))

        self._mapper.append(item)
        self.changed()

    def delete(self, key):
        self._mapper.delete(key)
        self.changed()


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
        return self._mapper_for(table).get(fields,
                                           order_by=order_by,
                                           descending=descending)

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
        self.changed(table)

    def append(self, table, item):
        t = self._tables[table]
        if isinstance(item, (list, tuple)):
            item = dict(zip(t.fields, item))

        self._mapper_for(table).append(item)
        self.changed(table)

    def delete(self, table, *key):
        t = self._tables[table]
        if len(key) == 1 and isinstance(key[0], dict):
            key = key[0]
        else:
            key = dict(zip(t.key, key))

        self._mapper_for(table).delete(key)
        self.changed(table)
