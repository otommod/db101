import psycopg2
from collections import namedtuple

from .schema import SCHEMA
from .observable import event
from .querybuilder import QueryBuilder


STATEMENT = """
SELECT Drug.name, BigPharma.name AS maker, Drug.formula, Sell.price FROM
  Drug
  JOIN BigPharma ON Drug.bigpharma_id = BigPharma.id
  JOIN Sell ON Drug.id = Sell.drug_id
WHERE Sell.pharmacy_id = %s;
"""

STATEMENT2 = """
SELECT Doctor.*, Patient.name FROM
  Doctor
  LEFT JOIN Patient ON Doctor.id = Patient.doctor_id;
"""

STATEMENT3 = """
SELECT Patient.name AS patient,
       Doctor.name AS doctor,
       Drug.name AS drug,
       date,
       dosage
FROM
  Prescription
  JOIN Patient ON Patient.id = Prescription.patient_id
  JOIN Doctor ON Doctor.id = Prescription.doctor_id
  JOIN Drug ON Drug.id = Prescription.drug_id
  JOIN Sell ON Sell.drug_id = Prescription.drug_id AND Sell.pharmacy_id = %s;
"""

AGGREGATE = """
SELECT COUNT(id) FROM Patient;
"""

GROUP_BY = """
SELECT COUNT(pharmacy_id)
FROM Sells
GROUP BY drug_id;
"""

ORDER_BY = """
SELECT *
FROM Contract
ORDER BY end_date;
"""

GROUP_BY_HAVING = """
SELECT COUNT(id)
FROM Contract
GROUP BY bigpharma_id;
HAVING end_date < %s;
"""

NESTED = """
SELECT name FROM Patient
    WHERE age > (SELECT exp FROM Doctor WHERE Doctor.id = Patient.doctor_id);
"""

NESTED2 = """
SELECT name FROM Doctor
    WHERE (SELECT AVG(age) FROM Patient WHERE Patient.doctor_id = Doctor.id) > 50;
"""


def valid_ident(ident):
    return ident.isidentifier()


def namedtuple_wrapper(fields):
    assert all(valid_ident(f) for f in fields)
    return namedtuple("row", fields)


class SQLDriver:
    # TODO: The first time a command is executed, a new transaction is created.
    # These need to be commited manually.  If not, the connection will sit in
    # an "idle in transaction" state, even for simple SELECTs and that's not
    # good.  Consider either autocommit mode or 'with' block on the connection
    # object.  This will not close the connection, rather, it will commit the
    # transaction.

    def __init__(self, conn):
        self.conn = conn

    def execute(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()


class Table:
    def __init__(self, db, name, key, fields):
        self.db = db
        self.name = name
        self.key = key
        self.fields = fields
        self.qb = QueryBuilder(name, key)

    @event
    def changed():
        pass

    def get(self, *fields, order_by="", descending=False):
        return self.db.get(self.name, *fields,
                           order_by=order_by, descending=descending)


class SQLModel:
    SCHEMA = SCHEMA

    def __init__(self, conn, result_wrapper=namedtuple_wrapper):
        self.driver = SQLDriver(conn)
        self.result_wrapper = result_wrapper

        self.tables = {}
        for name, table in self.SCHEMA.items():
            key = table["key"]
            if not isinstance(key, (list, tuple)):
                key = (key,)
            self.tables[name] = Table(self, name, key, table["fields"])

        self.changed.add_observer(self._dispatch_event)

    @event
    def changed(table):
        pass

    def _dispatch_event(self, table):
        if table in self.tables:
            self.tables[table].changed()

    def get(self, table, *fields, order_by="", descending=False):
        t = self.tables[table]
        if not fields:
            fields = t.fields
        q = t.qb.select(*fields, order_by=order_by, descending=descending)

        result_type = self.result_wrapper(fields)
        return [result_type(*i) for i in self.driver.execute(q)]

    def set(self, table, *ids, **updates):
        pass

    def delete(self, table, *ids):
        pass

    def append(self, table, *items):
        pass

    def patients_num(self):
        return self.driver.execute(AGGREGATE)[0][0]

    def contracts(self):
        return self.driver.execute(ORDER_BY)
