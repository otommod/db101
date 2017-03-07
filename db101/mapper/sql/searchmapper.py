from .helpers import MapperFactory


def read_from(filename):
    with open(filename) as f:
        return f.read()


class SearchMapper:
    ESCAPE_CHAR = "="

    def __init__(self, factory):
        # TODO: should be in the metaclass
        assert self.QUERY
        assert self.ARGS

        self.factory = factory

    @classmethod
    def _escape(cls, term):
        return (term.replace(cls.ESCAPE_CHAR, 2*cls.ESCAPE_CHAR)
                    .replace("%", cls.ESCAPE_CHAR + "%")
                    .replace("_", cls.ESCAPE_CHAR + "_"))

    def query(self, **kwargs):
        params = {"include_" + k: False for k in self.ARGS}
        params.update({k: None for k in self.ARGS})
        for k, v in kwargs.items():
            params[k] = v
            params["include_" + k] = True

        if self.ESCAPE:
            params = {self._escape(k) if k in self.ESCAPE else k: v
                      for k, v in params.items()}

        ok, results = self.factory.execute(self.QUERY, params)
        if not ok:
            return ok, results
        try:
            result_type = self.factory.result_wrapper(self.RETURNS)
            return True, [result_type(*i) for i in results]
        except TypeError:
            return ok, results


class PatientSearchMapper(SearchMapper):
    QUERY = read_from("sql/patient_search.pgsql")
    ARGS = {"our_pharmacy", "name", "maxage", "minage", "doctor", "address",
            "drug"}
    ESCAPE = {"name", "doctor", "address", "drug"}
    RETURNS = ("name", "age", "address", "doctor")


class DoctorSearchMapper(SearchMapper):
    QUERY = read_from("sql/doctor_search.pgsql")
    ARGS = {"our_pharmacy", "name", "specialty", "exp", "patient", "drug"}
    ESCAPE = {"name", "specialty", "patient", "drug"}
    RETURNS = ("name", "specialty", "exp")


class SearchMapperFactory(MapperFactory):
    def __call__(self, search_type):
        mappers = {
            "patient": PatientSearchMapper,
            "doctor": DoctorSearchMapper,
        }
        return mappers[search_type](self)
