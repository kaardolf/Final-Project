"""to_do_list doc string"""
# created basic crud statemts that iteract with mongo. 
# crated def fill_table() for the prefilled restraunts Kirsten had
# Change the data that is added (i have name, adress, and cuisine)

import os
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

def fill_table() -> None:
    """pre fill table with data"""
    #11 Brooklyn
    #1 Staten
    #2 Bronx
    resturant_1 = {"restaurant_id":"40356018","borough":"Brooklyn","cuisine":"American",}

    to_do.append(resturant_1)

    resturant_2 = {"name":"Wilken'S Fine Food", "borough":"Brooklyn","cuisine":"Delicatessen"}

    to_do.append(resturant_2)

#Remove
    resturant_3 = {"name":"Kosher Island", "borough":"Staten Island","cuisine":"Jewish/Kosher"}

    to_do.append(resturant_3)
    resturant_4 = {"name":"Bagels N Buns","borough":"Staten Island","cuisine":"Delicatessen"}

    to_do.append(resturant_4)

#remove
    resturant_5 = {"name":"Carvel Ice Cream","borough":"Staten Island",
                   "cuisine":"Ice Cream, Gelato, Yogurt, Ices"}

    to_do.append(resturant_5)

#keep
    resturant_6 = {"name":"B & M Hot Bagel & Grocery",
                   "borough":"Staten Island","cuisine":"Delicatessen"}
    to_do.append(resturant_6)





    try:
        collection.insert_many(to_do)
    except OperationFailure as ex:
        raise ex



def insert_one() -> None:
    """insert one item"""
    name = input("Eneter the name of restraunt: ")
    cuisine = input("Enter the type of cuisine served: ")
    adress = input("Enter the Adress for the restraunt: ")

    restraunt = {"name": name, "cuisine": cuisine, "adress": adress}

    try:
        collection.insert_one(restraunt)
        input("Inserted, Enter to exit: ")
    except OperationFailure as ex:
        print(ex)
        raise ex


def insert_many() -> None:
    """insert many items"""

    restraunts = []
    again = True

    while again is True:
        name = input("Eneter the name of restraunt: ")
        cuisine = input("Enter the type of cuisine served: ")
        adress = input("Enter the Adress for the restraunt: ")

        restraunt_temp = {"name": name, "cuisine": cuisine, "adress": adress}
        restraunts.append(restraunt_temp)

        more = input("Enter another recipie? [Y/N] ")
        if more == "Y" or more == "y":
            again = True
        else:
            again = False

    try:
        collection.insert_many(restraunts)
        input("Inserted, Enter to exit: ")
    except OperationFailure as ex:
        print(ex)
        raise ex
    


def read_all() -> None:
    """read_all"""

    result = collection.find()
    if result:
        for doc in result:
            name = doc['name']
            cuisine = doc['cuisine']
            adress = doc['adress']
            print(f'restraurant {name} at {adress} serves {cuisine}')
        input("Enter to exit: ")
    else:
        print('No restaurants found. ')
        input("Enter to exit: ")


def read_one() -> None:
    """read_one"""

    restaurant_name = input("Enter the restaurant name: ")
    restaurant = collection.find_one({"name": restaurant_name})

    if restaurant is not None:
        print(restaurant)
        input("Enter to exit: ")
    else:
        print("No restaurant found that has that name.")
        input("Enter to exit: ")


def update() -> None:
    """update data"""
    name = input("Enter the name of the restraunt you want to edit: ")

    change = input("Enter the item you would like to change [name, cuisine, adress]: ")

    if change == "name":
        update_data = input("Enter the new name: ")
        updated = collection.find_one_and_update({'name': name},
                                                {'$set': {'name': update_data}}, new=True)
    elif change == "cuisine":
        update_data = input("Enter the new cuisine: ")
        updated = collection.find_one_and_update({'name': name},
                                                 {'$set': {'cuisine': update_data}}, new=True)
    elif change == "adress":
        update_data = input("Enter the new adress: ")
        updated = collection.find_one_and_update({'name': name},
                                                {'$set': {'adress': update_data}}, new=True)

    if updated:
        print("Here's the updated restraunt data:")
        print(updated)
        input("Enter to exit: ")
    else:
        print("No restraunts found that match your perameter.")
        input("Enter to exit: ")


def delete() -> None:
    """delete data"""
    name = input("Enter the name of the restraunt you want to delete: ")
    result = collection.delete_many({"name": name})
    print(f'{result.deleted_count} records deleted!')
    input("Enter to exit: ")


def show_menu() -> int:
    """menu for ui"""
    options = """
    Insert data [1]
    Insert mutiple [2]
    Read all [3]
    Read one [4]
    update data [5]
    delete data [6]
    exit [7]
    """

    os.system("clear")
    print(options)
    choice = input("Enter option [1-7]: ")

    while True:
        if choice.isdecimal():
            opt = int(choice)
        if 1 <= opt <= 7:
            return int(opt)
        os.system("clear")
        print(options)
        choice = input("Enter a valid option[1-6]: ")


def main() -> None:
    """Main driver"""
    while True:
        choice = show_menu()
        if choice == 1:
            insert_one()
        elif choice == 2:
            insert_many()
        elif choice == 3:
            read_all()
        elif choice == 4:
            read_one()
        elif choice == 5:
            update()
        elif choice == 6:
            delete()
        elif choice == 7:
            exit(0)
