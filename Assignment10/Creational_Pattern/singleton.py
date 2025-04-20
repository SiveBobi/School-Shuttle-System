class DatabaseConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DatabaseConnection, cls).__new__(cls)
            cls.__instance.connection = "Connected to DB"
        return cls.__instance

    def get_connection(self):
        return self.connection
