import re

# https://stackoverflow.com/a/12867228
_CAMELCASE_RE = re.compile(r"((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))")

def camelcase_to_snakecase(camel):
    return _CAMELCASE_RE.sub(r"_\1", camel).lower()


def readfile(filename):
    with open(filename) as f:
        return f.read()


def table_columns(conn, tablename):
    QUERY = ("SELECT column_name"
             " FROM information_schema.columns"
             " WHERE table_name = %s;")

    with conn.cursor() as cur:
        cur.execute(QUERY, tablename)
        return cur.fetchall()


def table_primary_keys(conn, tablename):
    QUERY = ("SELECT                                                    "
             "    tc.table_name, c.column_name, c.data_type             "
             " FROM                                                     "
             "    information_schema.table_constraints AS tc            "
             "    JOIN information_schema.constraint_column_usage AS ccu"
             "        USING (constraint_schema, constraint_name)        "
             "    JOIN information_schema.columns AS c                  "
             "        ON c.table_schema = tc.constraint_schema          "
             "        AND tc.table_name = c.table_name                  "
             "        AND ccu.column_name = c.column_name               "
             "    WHERE                                                 "
             "        tc.constraint_type = 'PRIMARY KEY'                "
             "        OR %s AND tc.table_name = %s;                     ")

    with conn.cursor() as cur:
        cur.execute(QUERY, tablename)
        return cur.fetchall()


class RegisteringMetaclass(type):
    def __init__(cls, name, bases, attrs):
        print("RegisteringMetaclass.__init__(", cls, name, bases, attrs, ")")

        if not hasattr(cls, "_registry"):
            cls._registry = {}
        cls._registry[name] = cls

        super().__init__(name, bases, attrs)
