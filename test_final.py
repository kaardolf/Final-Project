"""Unittesting
"""
import unittest
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi

path_to_certificate = 'cert.pem'

uri = ('mongodb+srv://cluster0.7kjaziu.mongodb.net/?authSource=%24'
       'external&authMechanism=MONGODB-X509&retryWrites=true&w=majority')
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))  # type: ignore
db = client['final-project']
collection = db['to_do']
doc_count = collection.count_documents({})


class TestFinal(unittest.TestCase):
    def test_fill_table(self):
        try:
            db.validate_collection("to_do")
        except pymongo.errors.OperationFailure:
            print("This collection doesn't exist")
