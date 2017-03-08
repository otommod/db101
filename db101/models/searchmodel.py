from ..observable import eventsource


class SearchResults:
    def __init__(self, fields, searcher):
        pass


class Searcher:
    def __init__(self, mapper):
        self._mapper = mapper

        self._searches = {}
        self.changed.add_observer(self._dispatch_to_search)

    @eventsource
    def changed(search_type):
        pass

    def _dispatch_to_search(self, search_type):
        self._searches[search_type].changed()

    def search(self, what_for, params):
        cleaned_params = {k: v for k, v in params.items() if v == 0 or v}
        self._mapper.do(what_for, cleaned_params)
