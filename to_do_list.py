import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import OperationFailure

path_to_certificate = 'cert.pem'

uri = ('mongodb+srv://cluster0.7kjaziu.mongodb.net/?authSource=%24'
       'external&authMechanism=MONGODB-X509&retryWrites=true&w=majority')
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
db = client['final-project']
collection = db['to_do']
doc_count = collection.count_documents({})
#print(doc_count)



to_do = []




def fill_table() -> None:
    """pre fill table with data"""
    resturant_1 = {
        "name": "Reif's travern",
        "borough": "Manhattan",
        "cuisine": "American"}
    to_do.append(resturant_1)

    resturant_2 = {
        "name": "Regina Caterers",
        "borough": "Brooklyn",
        "cuisine": "American"}
    to_do.append(resturant_2)

    resturant_3 = {
        "name": "Maloney's bar",
        "borough": "Queens",
        "cuisine": "American"}
    to_do.append(resturant_3)

    resturant_4 = {
        "name": "Denino's Pizzeria Tavern",
        "borough": "Staten Island",
        "cuisine": "Pizza"}
    to_do.append(resturant_4)

    resturant_5 = {
        "name": "Jack's Pizza and pasta",
        "borough": "Queens",
        "cuisine": "Pizza"}
    to_do.append(resturant_5)

    resturant_6 = {
        "name": "Fascati's Pizzeria",
        "borough": "Brooklyn",
        "cuisine": "Pizza"}
    to_do.append(resturant_6)

    resturant_7 = {
        "name": "Killarney Rose",
        "borough": "Manhattan",
        "cuisine": "Irish"}
    to_do.append(resturant_7)

    resturant_8 = {
        "name": "O'Hanlon's Pub",
        "borough": "Queens",
        "cuisine": "Irish"}
    to_do.append(resturant_8)

    resturant_9 = {
        "name": "Mcdwyers Rub",
        "borough": "Bronx",
        "cuisine": "Irish"}
    to_do.append(resturant_9)

    resturant_10 = {
        "name": "Piccola Venezia",
        "borough": "Queens",
        "cuisine": "Italian"}
    to_do.append(resturant_10)

    resturant_11 = {
        "name": "Marina Cafe",
        "borough": "Staten Island",
        "cuisine": "Italian"}
    to_do.append(resturant_11)

    resturant_12 = {
        "name": "Forlinis Resturant",
        "borough": "Manhattan",
        "cuisine": "Italian"}
    to_do.append(resturant_12)

    resturant_13 = {
        "name": "Cuchifrito",
        "borough": "Manhattan",
        "cuisine": "Mexican"}
    to_do.append(resturant_13)

    resturant_14 = {
        "name": "Casa Pepe",
        "borough": "Brooklyn",
        "cuisine": "Mexican"}
    to_do.append(resturant_14)

    resturant_15 = {
        "name": "Mexico Lindo Resturant",
        "borough": "Manhattan",
        "cuisine": "Mexican"}
    to_do.append(resturant_15)

    resturant_16 = {
        "name": "Wilken'S Fine Food",
        "borough": "Brooklyn",
        "cuisine": "Delicatessen"}
    to_do.append(resturant_16)

    resturant_17 = {
        "name": "Plaza bagels and deli",
        "borough": "Staten Island",
        "cuisine": "Delicatessen"}
    to_do.append(resturant_17)

    resturant_18 = {
        "name": "B & M Hot Bagel & Grocery",
        "borough": "Staten Island",
        "cuisine": "Delicatessen"}
    to_do.append(resturant_18)


    try:
        collection.insert_many(to_do)
    except OperationFailure as ex:
        raise ex

def number_of_documents():
    if doc_count == 0:
        print("Collection is empty. Fill the collection")
    elif doc_count != 0:
        print("Collection is filled")

number_of_documents() #make a section in menu

fill_table() #Make a section in menu




    