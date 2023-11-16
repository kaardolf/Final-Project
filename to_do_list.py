from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import OperationFailure

path_to_certificate = 'cert.pem'

uri = "mongodb+srv://cluster0.7kjaziu.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
db = client['final-project']
collection = db['to_do']
doc_count = collection.count_documents({})
print(doc_count)

to_do = []

resturant_1 = {"restaurant_id":"40356018","borough":"Brooklyn","cuisine":"American",}

to_do.append(resturant_1)

resturant_2 = {"name":"Wilken'S Fine Food", "borough":"Brooklyn","cuisine":"Delicatessen"}

to_do.append(resturant_2)

try:
    collection.insert_many(to_do)
except OperationFailure as ex:
    raise ex







