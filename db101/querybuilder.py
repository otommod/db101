from psycopg2.sql import SQL, Identifier


class QueryBuilder:
    def __init__(self, tablename):
        self.table = Identifier(tablename)

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

    def insert(self, data):
        pass

    def insert_many(self, values):
        "INSERT INTO {0} ({1}) VALUES {2};"

        # value_tuples = SQL(", ").join(values)

    def update(self, key_field, field):
        if not isinstance(key_field, (list, tuple)):
            key_field = [key_field]

        where = SQL(" AND ").join(
            SQL("{0} = %s").format(Identifier(f)) for f in key_field)

        return SQL("UPDATE {0} SET {1} = %s WHERE {2};").format(
            self.table, Identifier(field), where)

    def delete(self, key_field):
        if not isinstance(key_field, (list, tuple)):
            key_field = [key_field]

        where = SQL(" AND ").join(
            SQL("{0} = %s").format(Identifier(f)) for f in key_field)

        return SQL("DELETE FROM {0} WHERE {1};").format(
            self.table, where)
