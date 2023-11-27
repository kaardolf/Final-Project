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

#American Manhattan- Reif's travern
#Done #American Brooklyn- Regina Caterers
#American Queens- Maloney's bar
#Pizza Staten Island- Denino's Pizzeria Tavern
#Pizza Queens- Jack's Pizza and pasta
#Pizza Brooklyn- Fascati's Pizzeria
#Irish Manhattan - Killarney Rose
#Irish Queens - O'Hanlon's Pub
#Irish Bronx - Mcdwyers Rub (121)
#Italian Queens - Piccola Venezia
#Italian Staten Island - Marina Cafe
#Italian Manhattan - Forlinis Resturant
#Mexican Manhattan - Cuchifrito
#Mexican Brooklyn - Casa Pepe
#Mexican Manhattan - Mexico Lindo Resturant
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








