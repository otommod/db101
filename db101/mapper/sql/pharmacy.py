from .helpers import MapperFactory, read_from


class SQLPharmacy(MapperFactory):
    QUERIES = {
        "drugs_on_sale": read_from("sql/pharmacy/drugs_on_sale.pgsql"),
    }

    def __call__(self, query_name, params):
        return self.execute(self.QUERIES[query_name], params)
