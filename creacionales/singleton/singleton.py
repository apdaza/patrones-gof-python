class Singleton():

    _instance = None

    @classmethod
    def get_instance(cls): # Constructor alternativo que retorna una nueva instancia
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
