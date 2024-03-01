from pymongo import MongoClient

class MongoDB:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client.get_database()

mongo = MongoDB("mongodb://localhost:27017/Estudiante")  # Reemplaza con tu URI de MongoDB
