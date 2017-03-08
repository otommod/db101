from ..helpers import camelcase_to_snakecase, RegisteringMetaclass
from ..observable import eventsource
from .table import Table


class ModelMetaclass(type):
    def __init__(cls, name, bases, attrs):
        print("ModelMetaclass.__init__(", cls, name, bases, attrs, ")")

        cls.Query = RegisteringMetaclass(
            "Query", (cls.Query,), {})
        cls.Query._registry = {}

        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print("ModelMetaclass.__call__(", args, kwargs, ")")

        self = type.__call__(cls, *args, **kwargs)
        for n, q in self.Query._registry.items():
            setattr(self, camelcase_to_snakecase(n), q(n, self))

        print("Model.Query._registry", self.Query._registry.keys())
        return self


class Model(metaclass=ModelMetaclass):
    class Query(metaclass=RegisteringMetaclass):
        _registry = {}

        def __init__(self, name, model):
            self.name = name
            self.model = model

        def __call__(self, params=None):
            return Table(self.RETURNS,
                         self.model._execute(self, params))

        def validate(cls, named_params):
            for p, v in named_params.items():
                if p not in cls.ARGUMENTS:
                    return False
                try:
                    cls.ARGUMENTS[p](v)
                    return True
                except ValueError:
                    return False

    def __init__(self, mapper, baked_params=None):
        self._mapper = mapper
        self._baked_params = frozenset((baked_params or {}).items())

    def _execute(self, query, params=None):
        all_params = {}
        all_params.update(self._baked_params)
        all_params.update(params or {})

        # if not all(p in query.ARGUMENTS for p in all_params):
        #     unknown_args = all_params.keys() - query.ARGUMENTS.keys()
        #     raise QueryValidationError(
        #         "No such arguments %(args)s for query %(query)s",
        #         unknown_args, queryname)
        # if not query.validate(all_params):
        #     raise QueryValidationError(
        #         "Invalid arguments %(args)s for query %(query)s",
        #         all_params, queryname)

        return self._mapper(query, all_params)
