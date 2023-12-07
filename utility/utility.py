"""to_do_list doc string"""

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import OperationFailure


path_to_certificate = 'utility/cert.pem'

uri = ('mongodb+srv://cluster0.7kjaziu.mongodb.net/?authSource=%24'
       'external&authMechanism=MONGODB-X509&retryWrites=true&w=majority')
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))  # type: ignore
db = client['final-project']
collection = db['to_do']
doc_count = collection.count_documents({})


def db_insert_one(data) -> None:
    """create one"""

    try:
        collection.insert_one(data)
    except OperationFailure as ex:
        print(ex)
        raise ex


def db_insert_many(data) -> None:
    """create mutiple"""
    try:
        collection.insert_many(data)
    except OperationFailure as ex:
        raise ex


def db_update(name, update_data, newdata) -> any:
    """update"""
    return collection.find_one_and_update(
        {'name': name},
        {'$set': {update_data: newdata}},
        new=True)


def db_read_all() -> any:
    """read all"""
    return collection.find()


def db_read_one(restaurant_name) -> any:
    """read one"""
    return collection.find_one({"name": restaurant_name})


def db_delte(data) -> any:
    """delete"""
    return collection.delete_many({"name": data})


def db_count() -> any:
    """counts doc in database"""
    return collection.count_documents({})
