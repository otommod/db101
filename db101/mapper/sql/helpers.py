from collections import namedtuple

from .driver import PostgresDriver


def namedtuple_wrapper(fields):
    assert all(f.isidentifier() for f in fields)
    return namedtuple("row", fields)


class MapperFactory:
    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.conn = conn
        self.driver = PostgresDriver(conn)
        self.result_wrapper = result_wrapper

    def execute(self, query, params=None):
        return self.driver.execute(query, params)
