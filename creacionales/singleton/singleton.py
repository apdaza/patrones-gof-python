class Singlethon():
    __instance__ = None

    def __new__(cls):
        if cls.__instance__ is None:
            cls.__instance__ = super(SingletonIfNone, cls).__new__(cls)
        return cls.__instance__
