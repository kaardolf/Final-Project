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

#"name":"Reif's travern", "borough":"Manhattan","cuisine":"American"
#Done #American Brooklyn- Regina Caterers
#"name":"Maloney's bar", "borough":"Queens","cuisine":"American"
#"name":"Denino's Pizzeria Tavern", "borough":"Staten Island","cuisine":"Pizza"
#"name":"Jack's Pizza and pasta", "borough":"Queens","cuisine":"Pizza"
#"name":"Fascati's Pizzeria", "borough":"Brooklyn","cuisine":"Pizza"
#"name":"Killarney Rose", "borough":"Manhattan","cuisine":"Irish"
#"name":"O'Hanlon's Pub", "borough":"Queens","cuisine":"Irish"
#"name":"Mcdwyers Rub", "borough":"Bronx","cuisine":"Irish"
#"name":"Piccola Venezia","borough":"Queens","cuisine":"Italian"
#"name":"Marina Cafe","borough":"Staten Island","cuisine":"Italian"
#"name": "Forlinis Resturant", "borough":"Manhattan","cuisine":"Italian"
#"name":"Cuchifrito","borough":"Manhattan","cuisine":"Mexican"
#"name":"Casa Pepe","borough":"Brooklyn","cuisine":"Mexican"
#"name":"Mexico Lindo Resturant","borough":"Manhattan","cuisine":"Mexican"
#Done #Delicatessen Staten Island - Plaza bagels and deli
#Done #Delicatessen Brooklyn - Wilken's Fine food
#Done #Delicatessen Staten Island - B & M Hot Bagel and Grocery

#Update to be "name":"Rivviera Caterer" not "restaurant_id":"40356018"
resturant_1 = {"restaurant_id":"40356018","borough":"Brooklyn","cuisine":"American",}

to_do.append(resturant_1)
#Keep
resturant_2 = {"name":"Wilken'S Fine Food", "borough":"Brooklyn","cuisine":"Delicatessen"}

to_do.append(resturant_2)

#Remove
resturant_3 = {"name":"Kosher Island", "borough":"Staten Island","cuisine":"Jewish/Kosher"}

to_do.append(resturant_3)

#keep but name is Plaza bagels and deli
resturant_4 = {"name":"Bagels N Buns","borough":"Staten Island","cuisine":"Delicatessen"}

to_do.append(resturant_4)

#remove
resturant_5 = {"name":"Carvel Ice Cream","borough":"Staten Island","cuisine":"Ice Cream, Gelato, Yogurt, Ices"}

to_do.append(resturant_5)

#keep
resturant_6 = {"name":"B & M Hot Bagel & Grocery","borough":"Staten Island","cuisine":"Delicatessen"}
to_do.append(resturant_6)





try:
    collection.insert_many(to_do)
except OperationFailure as ex:
    raise ex








