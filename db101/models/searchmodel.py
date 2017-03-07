from ..observable import eventsource


class SearchModel:
    def __init__(self, mapper_factory):
        self.mapper_factory = mapper_factory

    @eventsource
    def changed(search_type):
        pass

    def _mapper_for(self, search_type):
        return self.mapper_factory(search_type)

    def patient_search(self, **kwargs):
        return self._mapper_for("patient").query(**kwargs)

    def doctor_search(self, **kwargs):
        return self._mapper_for("doctor").query(**kwargs)

    # def patient_search(self, *args):
    #     self._mapper_for(self, "patient").query(*args)

    # def patient_search(self, *args):
    #     self._mapper_for(self, "patient").query(*args)
