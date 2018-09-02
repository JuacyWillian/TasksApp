class Singleton(object):
    _instance = None

    def __new__(cls, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, **kwargs)
        return cls._instance
