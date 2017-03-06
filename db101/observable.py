# https://stackoverflow.com/a/1926336
# http://simeonfranklin.com/talk/descriptors.html


class boundeventsource(object):
    def __init__(self):
        self._observers = []

    def add_observer(self, obs):
        self._observers.append(obs)

    def __call__(self, *args, **kwargs):
        for f in self._observers:
            f(*args, **kwargs)


class eventsource(object):
    def __init__(self, method):
        self.__doc__ = method.__doc__
        self.__name__ = method.__name__

    def __get__(self, obj, objtype):
        print("eventsource.__get__(%s, %s)" % (obj, objtype))

        if obj is None:
            return self
        if self.__name__ not in obj.__dict__:
            obj.__dict__[self.__name__] = boundeventsource()
        return obj.__dict__[self.__name__]
