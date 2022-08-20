from config import Configuration
from pymongo import MongoClient

class Database:
    __instance = None
    _mongoClientInstance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def col(self, name):
        col = self.db()[name]

        return col
    
    def client(self):
        if self._mongoClientInstance is None:
            config = Configuration()

            address = config.db_address()
            port = config.db_port()

            # "mongodb://192.168.1.190:27017"
            mongoDbAddress = f'{address}:{port}'

            self._mongoClientInstance = MongoClient(mongoDbAddress)

        return self._mongoClientInstance

    def db(self):
        database = self.client()["comida-db"]

        return database