"""to_do_list doc string"""

import os
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
print(doc_count)

to_do = []


def fill_table() -> None:
    """pre fill table with data"""
    resturant_1 = {
        "name": "Reif's travern",
        "borough": "Manhattan",
        "cuisine": "American",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_1)

    resturant_2 = {
        "name": "Regina Caterers",
        "borough": "Brooklyn",
        "cuisine": "American",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_2)

    resturant_3 = {
        "name": "Maloney's bar",
        "borough": "Queens",
        "cuisine": "American",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_3)

    resturant_4 = {
        "name": "Denino's Pizzeria Tavern",
        "borough": "Staten Island",
        "cuisine": "Pizza",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_4)

    resturant_5 = {
        "name": "Jack's Pizza and pasta",
        "borough": "Queens",
        "cuisine": "Pizza",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_5)

    resturant_6 = {
        "name": "Fascati's Pizzeria",
        "borough": "Brooklyn",
        "cuisine": "Pizza",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_6)

    resturant_7 = {
        "name": "Killarney Rose",
        "borough": "Manhattan",
        "cuisine": "Irish",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_7)

    resturant_8 = {
        "name": "O'Hanlon's Pub",
        "borough": "Queens",
        "cuisine": "Irish",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_8)

    resturant_9 = {
        "name": "Mcdwyers Rub",
        "borough": "Bronx",
        "cuisine": "Irish",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_9)

    resturant_10 = {
        "name": "Piccola Venezia",
        "borough": "Queens",
        "cuisine": "Italian",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_10)

    resturant_11 = {
        "name": "Marina Cafe",
        "borough": "Staten Island",
        "cuisine": "Italian",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_11)

    resturant_12 = {
        "name": "Forlinis Resturant",
        "borough": "Manhattan",
        "cuisine": "Italian",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_12)

    resturant_13 = {
        "name": "Cuchifrito",
        "borough": "Manhattan",
        "cuisine": "Mexican",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_13)

    resturant_14 = {
        "name": "Casa Pepe",
        "borough": "Brooklyn",
        "cuisine": "Mexican",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_14)

    resturant_15 = {
        "name": "Mexico Lindo Resturant",
        "borough": "Manhattan",
        "cuisine": "Mexican",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_15)

    resturant_16 = {
        "name": "Wilken'S Fine Food",
        "borough": "Brooklyn",
        "cuisine": "Delicatessen",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_16)

    resturant_17 = {
        "name": "Plaza bagels and deli",
        "borough": "Staten Island",
        "cuisine": "Delicatessen",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_17)

    resturant_18 = {
        "name": "B & M Hot Bagel & Grocery",
        "borough": "Staten Island",
        "cuisine": "Delicatessen",
        "ave_rating": None,
        "ratings": [int],
        "comments": [str]}
    to_do.append(resturant_18)

    try:
        collection.insert_many(to_do)
    except OperationFailure as ex:
        raise ex


def insert_review() -> None:
    """inserts new reveiw for restraunt"""

    name = input("Eneter the name of restraunt you want to reveiw: ")
    info = collection.find_one({"name": name})

    if info is not None:
        ratings = info['ratings']
        comments = info['comments']
        temp_rating = input("Enter rating for the restraunt [1-5]:")
        valid_rating = True
        while valid_rating:
            if temp_rating.isdigit():
                if (int(temp_rating) <= 0) or (int(temp_rating) >= 6):
                    print("Input not between 1 and 5")
                    temp_rating = input("Enter rating "
                                        "for the restraunt [1-5]:")
                else:
                    valid_rating = False
            else:
                print("Input not integer")
                temp_rating = input("Enter rating for the restraunt [1-5]:")

        temp_comment = input("Enter any commnets for the restraunt:")

        ratings.append(int(temp_rating))
        comments.append(temp_comment)

        new_rating = 0

        for i in ratings:
            new_rating = new_rating + i
        new_rating = new_rating / len(ratings)

        collection.find_one_and_update(
            {'name': name},
            {'$set': {'ave_rating': new_rating}},
            new=True)
        collection.find_one_and_update(
            {'name': name},
            {'$set': {'ratings': ratings}},
            new=True)
        collection.find_one_and_update(
            {'name': name},
            {'$set': {'comments': comments}},
            new=True)
    else:
        print("No restaurant found that has that name.")
        input("Enter to exit: ")


def insert_one() -> None:
    """insert one item"""
    name = input("Eneter the name of restraunt: ")
    cuisine = input("Enter the type of cuisine served: ")
    borough = input("Enter the borough for the restraunt: ")

    restraunt = {"name": name, "cuisine": cuisine, "borough": borough,
                 "ave_rating": None, "ratings": [int], "comments": [str]}

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
        borough = input("Enter the borough for the restraunt: ")

        restraunt_temp = {"name": name, "cuisine": cuisine, "borough": borough,
                          "ave_rating": None, "ratings": [int], "comments": [str]}

        restraunts.append(restraunt_temp)

        more = input("Enter another restraunt? [Y/N]: ")
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
            borough = doc['borough']
            ave_rating = doc['ave_rating']
            rating = doc['ratings']
            comments = doc['comments']
            print(f'{name} in {borough} serves '
                  f'{cuisine}, and it rated {ave_rating}/5')
            if ave_rating is not None:
                rate_reveiws = input("would you like to see the "
                                     "reveiws for this restraunt? [Y/N]:")
                if rate_reveiws == "Y" or rate_reveiws == "y":
                    for i, rating in enumerate(rating):
                        print(f'{rating}/5. Comments: {comments[i]}')
        input("Enter to exit: ")
    else:
        print('No restaurants found. ')
        input("Enter to exit: ")


def read_one() -> None:
    """read_one"""

    restaurant_name = input("Enter the restaurant name: ")
    restaurant = collection.find_one({"name": restaurant_name})

    if restaurant is not None:
        name = restaurant['name']
        cuisine = restaurant['cuisine']
        borough = restaurant['borough']
        ave_rating = restaurant['ave_rating']
        rating = restaurant['ratings']
        comments = restaurant['comments']
        print(f'{name} in {borough} serves'
              f'{cuisine}, and it rated {ave_rating}/5')
        if ave_rating is not None:
            rate_reveiws = input("would you like to see the "
                                 "reveiws for this restraunt? [Y/N]:")
            if rate_reveiws == "Y" or rate_reveiws == "y":
                for i, rating in enumerate(rating):
                    print(f'{rating}/5. Comments: {comments[i]}')

        input("Enter to exit: ")
    else:
        print("No restaurant found that has that name.")
        input("Enter to exit: ")


def update() -> None:
    """update data"""
    name = input("Enter the name of the restraunt you want to edit: ")

    change = input("Enter the item you would like to change."
                   "[name, cuisine, borough]: ")

    if change == "name":
        update_data = input("Enter the new name: ")
        updated = collection.find_one_and_update(
            {'name': name},
            {'$set': {'name': update_data}},
            new=True)
    elif change == "cuisine":
        update_data = input("Enter the new cuisine: ")
        updated = collection.find_one_and_update(
            {'name': name},
            {'$set': {'cuisine': update_data}},
            new=True)
    elif change == "borough":
        update_data = input("Enter the new borough: ")
        updated = collection.find_one_and_update(
            {'name': name},
            {'$set': {'borough': update_data}},
            new=True)

    if updated:
        print("updated restraunt data.")
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
    Insert a review for a restraunt [1]
    Insert restraunt's data [2]
    Insert mutiple restraunts [3]
    Read all restraunt's data [4]
    Read one restraunt's data [5]
    update restraunt's data [6]
    delete a restraunt [7]
    exit [8]
    """

    os.system("clear")
    print(options)
    choice = input("Enter option [1-8]: ")

    while True:
        if choice.isdigit():
            if 1 <= int(choice) <= 8:
                return int(choice)
            else:
                os.system("clear")
                print(options)
                choice = input("Enter a valid option[1-8]: ")
        else:
            os.system("clear")
            print(options)
            choice = input("Enter a valid option[1-8]: ")


def main() -> None:
    """Main driver"""
    while True:
        choice = show_menu()
        if choice == 1:
            insert_review()
        elif choice == 2:
            insert_one()
        elif choice == 3:
            insert_many()
        elif choice == 4:
            read_all()
        elif choice == 5:
            read_one()
        elif choice == 6:
            update()
        elif choice == 7:
            delete()
        elif choice == 8:
            exit(0)
