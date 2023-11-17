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

#11 Brooklyn
#1 Staten
#2 Bronx
resturant_1 = {"restaurant_id":"40356018","borough":"Brooklyn","cuisine":"American",}

to_do.append(resturant_1)

resturant_2 = {"name":"Wilken'S Fine Food", "borough":"Brooklyn","cuisine":"Delicatessen"}

to_do.append(resturant_2)

resturant_3 = {"name":"Kosher Island", "borough":"Staten Island","cuisine":"Jewish/Kosher"}

to_do.append(resturant_3)
resturant_4 = {"name":"Bagels N Buns","borough":"Staten Island","cuisine":"Delicatessen"}

to_do.append(resturant_4)

resturant_5 = {"name":"Carvel Ice Cream","borough":"Staten Island","cuisine":"Ice Cream, Gelato, Yogurt, Ices"}

to_do.append(resturant_5)

resturant_6 = {"name":"B & M Hot Bagel & Grocery","borough":"Staten Island","cuisine":"Delicatessen"}
to_do.append(resturant_6)

resturant_12 = {"name ": "Wendy'S", "borough" : "Brooklyn", "cuisine" : "Hamburgers"}

resturant_13 = {"name":"Morris Park Bake Shop", "borough":"Bronx","cuisine":"Bakery"}

resturant_14 = {"name":"Tov Kosher Kitchen","borough":"Queens","cuisine":"Jewish/Kosher"}

resturant_7 = {"name":"Brunos On The Boulevard","borough":"Queens","cuisine":"American"}

resturant_8 = {"name":"Regina Caterers","borough":"Brooklyn","cuisine":"American"}

resturant_9 = {"name":"Taste The Tropics Ice Cream","borough":"Brooklyn","cuisine":"Ice Cream, Gelato, Yogurt, Ices"}

resturant_10 = {"name":"Wild Asia","borough":"Bronx","cuisine":"American"}

resturant_11 = {"name":"C & C Catering Service","borough":"Brooklyn","cuisine":"American"}


try:
    collection.insert_many(to_do)
except OperationFailure as ex:
    raise ex







