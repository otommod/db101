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
        if not hasattr(term, "replace"):
            return term
        return (term.replace(cls.ESCAPE_CHAR, 2*cls.ESCAPE_CHAR)
                    .replace("%", cls.ESCAPE_CHAR + "%")
                    .replace("_", cls.ESCAPE_CHAR + "_"))

    def query(self, given_params):
        params = {k: None for k in self.ARGS}
        params.update({"include_" + k: False for k in self.ARGS})
        params.update({"include_" + k: True for k in given_params})
        params.update(given_params)

        if self.ESCAPE:
            params = {k: self._escape(v) if k in self.ESCAPE else v
                      for k, v in params.items()}

        print("SearchMapper.query", params)
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
