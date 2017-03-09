import os.path

from .table import Table


class Model():
    mapper_factory = None

    class Query():
        def __init__(self, name, model):
            # self.name = name
            self.model = model

        def __call__(self, params=None):
            return Table(self.returns,
                         self.model._execute(self, params))

        def validate(cls, named_params):
            for p, v in named_params.items():
                if p not in cls.arguments:
                    return False
                try:
                    cls.arguments[p](v)
                    return True
                except ValueError:
                    return False

    @classmethod
    def from_desc(cls, name, desc):
        subcls = type(cls)(name, (cls,), {"_queries": {}})
        for n, q in desc.items():
            query_name = os.path.basename(os.path.splitext(n)[0])
            qcls = type(subcls.Query)(query_name, (subcls.Query,), q.copy())
            subcls._queries[query_name] = qcls
        return subcls

    def __init__(self, baked_params=None):
        self._mapper = self.mapper_factory

        self._baked_params = frozenset((baked_params or {}).items())
        for n, q in self._queries.items():
            setattr(self, n, q(n, self))

    def _execute(self, query, params=None):
        all_params = {}
        all_params.update(self._baked_params)
        all_params.update(params or {})

        # if not all(p in query.arguments for p in all_params):
        #     unknown_args = all_params.keys() - query.arguments.keys()
        #     raise QueryValidationError(
        #         "No such arguments %(args)s for query %(query)s",
        #         unknown_args, queryname)
        # if not query.validate(all_params):
        #     raise QueryValidationError(
        #         "Invalid arguments %(args)s for query %(query)s",
        #         all_params, queryname)

        return self._mapper(query, all_params)
