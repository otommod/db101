from .driver import PostgresDriver
from .helpers import namedtuple_wrapper
# from .sqlquery import SQLQuery
from .queries import SQLQuery


class QueryResult:
    def __init__(self, execute, query, params=None):
        self._execute = execute
        self._query = query
        self._params = params

    def get(self, fields):
        return self._execute(self._query, self._params)


class QueryMapper:
    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.conn = conn
        self.driver = PostgresDriver(conn)
        self.result_wrapper = result_wrapper

    def execute(self, modelquery, params=None):
        query = SQLQuery._registry[type(modelquery).__name__]

        # FIXME
        query_obj = query()
        query_obj.ARGUMENTS = modelquery.ARGUMENTS
        query_obj.RETURNS = modelquery.RETURNS
        made_params = query_obj.prepare(params)

        return QueryResult(self.driver.execute, query.QUERY, made_params)
