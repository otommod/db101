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
