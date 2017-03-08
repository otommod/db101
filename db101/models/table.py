from ..observable import eventsource


class Table:
    def __init__(self, fields, mapper):
        self.fields = fields
        self._mapper = mapper

    @eventsource
    def changed():
        pass

    def get(self, *fields):
        if not fields:
            fields = self.fields
        return self._mapper.get(fields)
