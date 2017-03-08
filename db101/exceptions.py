class ModelError(Exception):
    pass


class InvalidKeyError(ModelError):
    pass


class InvalidOperationError(ModelError):
    def __init__(self, pgerror):
        self.msg = pgerror.pgerror


class QueryValidationError(ModelError):
    def __init__(self, query, invalid_args, msg=""):
        self.query = query
        self.invalid_args = invalid_args
        self.msg = msg % {
            "args": ", ".join("'%s'" % a for a in invalid_args),
            "query": query
        }
