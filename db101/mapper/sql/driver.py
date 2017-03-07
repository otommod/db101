import psycopg2


class PostgresDriver:
    # TODO: The first time a command is executed, a new transaction is created.
    # These need to be commited manually.  If not, the connection will sit in
    # an "idle in transaction" state, even for simple SELECTs and that's not
    # good.  Consider either autocommit mode or 'with' block on the connection
    # object.  This will not close the connection, rather, it will commit the
    # transaction.

    def __init__(self, conn):
        self.conn = conn
        self.conn.autocommit = True

    def execute(self, query, params=None):
        with self.conn.cursor() as cur:
            print(params)
            print(cur.mogrify(query, params).decode())

            try:
                cur.execute(query, params)
            except psycopg2.Error as e:
                return False, e

            try:
                return True, cur.fetchall()
            except psycopg2.ProgrammingError:
                return True, cur.rowcount
            except psycopg2.Error as e:
                return False, e
