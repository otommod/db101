from collections import namedtuple
from functools import partial

from ..observable import eventsource
from ..schema import SCHEMA
from ..exceptions import InvalidKeyError, InvalidOperationError
from .table import Table


class NamedTable(Table):
    mapper_factory = None

    @classmethod
    def loopup(cls, name):
        assert cls.mapper_factory

        schema = SCHEMA[name]
        return cls(name,
                   schema["key"],
                   schema["fields"],
                   cls.mapper_factory(name, schema["key"]))

    def __init__(self, name, keyfields, fields, mapper):
        super().__init__(fields, mapper)

        self.name = name
        if isinstance(keyfields, (tuple, list)):
            self.keyfields = keyfields.copy()
        else:
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
            item = dict(zip(self.fields, item))

        self._mapper.append(item)
        self.changed()

    def delete(self, key):
        self._mapper.delete(key)
        self.changed()
