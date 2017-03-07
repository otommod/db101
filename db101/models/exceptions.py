class ModelError(Exception):
    pass


class InvalidKeyError(ModelError):
    pass


class InvalidOperationError(ModelError):
    def __init__(self, pgerror):
        self.msg = pgerror.pgerror
