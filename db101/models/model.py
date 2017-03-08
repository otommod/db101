from ..helpers import camelcase_to_snakecase, RegisteringMetaclass
from ..observable import eventsource


class ModelMetaclass(type):
    def __init__(cls, name, bases, attrs):
        print("ModelMetaclass.__init__(", cls, name, bases, attrs, ")")

        cls.Query = RegisteringMetaclass(
            "Query", (cls.Query,), {})
        cls.Query._registry = {}

        super().__init__(name, bases, attrs)


class Model(metaclass=ModelMetaclass):
    class Query(metaclass=RegisteringMetaclass):
        _registry = {}

        def __init__(self, name, model):
            self.name = name
            self.model = model

        def __call__(self, params=None):
            return self.model._execute(self, params)

    def __init__(self, mapper, baked_params=None):
        self._mapper = mapper
        self._baked_params = frozenset((baked_params or {}).items())

        for name, cls in self.Query._registry.items():
            setattr(self,
                    camelcase_to_snakecase(name),
                    cls(name, self))
        self._queries = tuple(self.Query._registry.keys())
        print("Model._queries", self._queries)

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

        return self._mapper.execute(query, all_params)

    @eventsource
    def changed():
        pass
