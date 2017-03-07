def query(sql=None, *, from_file=None):
    print("query", sql, from_file, __name__, __file__)

    def decorator(func):
        print("query.decorator", sql, from_file, __name__, __file__)

        def inner(*args, **kwargs):
            print("query.inner", sql, from_file, __name__, __file__)
            return func(*args, **kwargs)
        return inner
    return decorator
