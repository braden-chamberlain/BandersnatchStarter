from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["Database"]

    def __init__(self, collection: str):
        """initializes the database with MongoDB"""
        self.collection = self.database[collection]

    def seed(self, amount):
        """Generates dictionaries of monsters and adds them to the database"""
        documents = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(documents)

    def reset(self):
        """Deletes all documents from collection"""
        self.collection.delete_many({})

    def count(self) -> int:
        """counts the number of documents in the collection"""
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        """converts collection into a pandas dataframe"""
        return DataFrame(self.collection.find({}))

    def html_table(self) -> str:
        if self.count() == 0:
            return 'None'
        else:
            return self.dataframe().to_html()
