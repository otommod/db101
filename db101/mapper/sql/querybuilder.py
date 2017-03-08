from psycopg2.sql import SQL, Identifier


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
