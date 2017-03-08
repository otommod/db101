from .helpers import MapperFactory, read_from


class SearchMapperFactory(MapperFactory):
    def __call__(self, search_type):
        mappers = {
            "patient": PatientSearchMapper,
            "doctor": DoctorSearchMapper,
        }
        return mappers[search_type](self)
