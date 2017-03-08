from .driver import PostgresDriver
from .helpers import namedtuple_wrapper
from .sqlquery import SQLQuery


class QueryMapper:
    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.conn = conn
        self.driver = PostgresDriver(conn)
        self.result_wrapper = result_wrapper

    def execute(self, modelquery, params=None):
        query = SQLQuery.ALL[type(modelquery).__name__]

        # FIXME
        query_obj = query()
        query_obj.ARGUMENTS = modelquery.ARGUMENTS
        query_obj.RETURNS = modelquery.RETURNS
        made_params = query_obj.prepare(params)

        print(query.QUERY, made_params)
        return self.driver.execute(query.QUERY, made_params)
