from ..observable import eventsource


SEARCH_SCHEMA = {
    "patient": ("name", "age", "address", "doctor"),
    "doctor": ("name", "specialty", "exp"),
}


class SearchModelResults:
    def __init__(self, name, fields, db):
        self.name = name
        self.fields = fields
        self._baked_args = {}
        self.db = db

    @eventsource
    def changed():
        pass

    def bake(self, **kwargs):
        self._baked_args.update(kwargs)

    def get(self, **kwargs):
        kwargs.update(self._baked_args)
        return self.db.get(self.name, **kwargs)


class SearchModel:
    def __init__(self, mapper_factory):
        self.mapper_factory = mapper_factory
        self.changed.add_observer(self._dispatch_to_search)

        self._searches = {}
        for search, fields in SEARCH_SCHEMA.items():
            assert search.isidentifier()
            searchmodel = SearchModelResults(search, fields, self)
            self._searches[search] = searchmodel
            setattr(self, search, searchmodel)

    @eventsource
    def changed(search_type):
        pass

    def _dispatch_to_search(self, search_type):
        self._searches[search_type].changed()

    def _mapper_for(self, search_type):
        return self.mapper_factory(search_type)

    def get(self, search_type, **kwargs):
        ok, results = self._mapper_for(search_type).query(
            {k: v for k, v in kwargs.items() if v == 0 or v})
        if not ok:
            raise results
        return results
