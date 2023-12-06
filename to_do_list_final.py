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
                     server_api=ServerApi('1'))  # type: ignore
db = client['final-project']
collection = db['to_do']
doc_count = collection.count_documents({})


to_do = []


def fill_table() -> None:
    """pre fill table with data"""
    restaurant_1 = {
        "name": "Reif's travern",
        "borough": "Manhattan",
        "cuisine": "American",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_1)

    restaurant_2 = {
        "name": "Regina Caterers",
        "borough": "Brooklyn",
        "cuisine": "American",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_2)

    restaurant_3 = {
        "name": "Maloney's bar",
        "borough": "Queens",
        "cuisine": "American",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_3)

    restaurant_4 = {
        "name": "Denino's Pizzeria Tavern",
        "borough": "Staten Island",
        "cuisine": "Pizza",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_4)

    restaurant_5 = {
        "name": "Jack's Pizza and pasta",
        "borough": "Queens",
        "cuisine": "Pizza",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_5)

    restaurant_6 = {
        "name": "Fascati's Pizzeria",
        "borough": "Brooklyn",
        "cuisine": "Pizza",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_6)

    restaurant_7 = {
        "name": "Killarney Rose",
        "borough": "Manhattan",
        "cuisine": "Irish",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_7)

    restaurant_8 = {
        "name": "O'Hanlon's Pub",
        "borough": "Queens",
        "cuisine": "Irish",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_8)

    restaurant_9 = {
        "name": "Mcdwyers Rub",
        "borough": "Bronx",
        "cuisine": "Irish",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_9)

    restaurant_10 = {
        "name": "Piccola Venezia",
        "borough": "Queens",
        "cuisine": "Italian",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_10)

    restaurant_11 = {
        "name": "Marina Cafe",
        "borough": "Staten Island",
        "cuisine": "Italian",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_11)

    restaurant_12 = {
        "name": "Forlinis Resturant",
        "borough": "Manhattan",
        "cuisine": "Italian",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_12)

    restaurant_13 = {
        "name": "Cuchifrito",
        "borough": "Manhattan",
        "cuisine": "Mexican",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_13)

    restaurant_14 = {
        "name": "Casa Pepe",
        "borough": "Brooklyn",
        "cuisine": "Mexican",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_14)

    restaurant_15 = {
        "name": "Mexico Lindo Resturant",
        "borough": "Manhattan",
        "cuisine": "Mexican",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_15)

    restaurant_16 = {
        "name": "Wilken'S Fine Food",
        "borough": "Brooklyn",
        "cuisine": "Delicatessen",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_16)

    restaurant_17 = {
        "name": "Plaza bagels and deli",
        "borough": "Staten Island",
        "cuisine": "Delicatessen",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_17)

    restaurant_18 = {
        "name": "B & M Hot Bagel & Grocery",
        "borough": "Staten Island",
        "cuisine": "Delicatessen",
        "ave_rating": None,
        "ratings": [],
        "comments": []}  # type: ignore
    to_do.append(restaurant_18)

    try:
        collection.insert_many(to_do)
    except OperationFailure as ex:
        raise ex


def number_of_documents() -> None:
    """Counts number of documents in DB
    """
    if doc_count == 0:
        print("Collection is empty. Fill the collection")
        input("Enter to exit: ")
        input("Enter to exit: ")
    elif doc_count != 0:
        print("Collection is filled with", doc_count, "documents")
        input("Enter to exit: ")
        input("Enter to exit: ")


def insert_review() -> None:
    """inserts new review for  restaurant"""

    name = input("Enter the name of restaurant you want to review: ")
    info = collection.find_one({"name": name})

    if info is not None:
        ratings = info['ratings']
        comments = info['comments']
        temp_rating = input("Enter rating for the restaurant [1-5]:")
        valid_rating = False
        while not valid_rating:
            if temp_rating.isdigit():
                if (int(temp_rating) <= 0) or (int(temp_rating) >= 6):
                    print("Input not between 1 and 5")
                    temp_rating = input("Enter rating "
                                        "for the restaurant [1-5]:")
                else:
                    valid_rating = True
                    valid_rating = True
            else:
                print("Input not integer")
                temp_rating = input("Enter rating for the restaurant [1-5]:")

        temp_comment = input("Enter any comments for the restaurant:")

        ratings.append(int(temp_rating))
        comments.append(temp_comment)

        new_rating = 0

        for i in ratings:
            new_rating = new_rating + i
        new_rating = new_rating / len(ratings)  # type: ignore

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
    name = input("Enter the name of restaurant: ")
    cuisine = input("Enter the type of cuisine served: ")
    borough = input("Enter the borough for the restaurant: ")

    restaurant = {"name": name,
                  "cuisine": cuisine,
                  "borough": borough,
                  "ave_rating": None,
                  "ratings": [],
                  "comments": []}  # type: ignore

    try:
        collection.insert_one(restaurant)
        input("Inserted, Enter to exit: ")
    except OperationFailure as ex:
        print(ex)
        raise ex


def insert_many() -> None:
    """insert many items"""

    restaurants = []
    again = True

    while again is True:
        name = input("Enter the name of restaurant: ")
        cuisine = input("Enter the type of cuisine served: ")
        borough = input("Enter the borough for the restaurant: ")

        restaurant_temp = {
            "name": name,
            "cuisine": cuisine,
            "borough": borough,
            "ave_rating": None,
            "ratings": [],
            "comments": []}  # type: ignore

        restaurants.append(restaurant_temp)

        more = input("Enter another restaurant? [Y/N]: ")
        if more == "Y" or more == "y":
            again = True
        else:
            again = False

    try:
        collection.insert_many(restaurants)
        input("Inserted, Enter to exit: ")
    except OperationFailure as ex:
        print(ex)
        raise ex


def insert_data() -> None:
    """Insert restaurant data"""
    user_selection = input("Enter the data you would like to insert:\n"
                           "[1] Insert restaurant review\n"
                           "[2] Insert data for one restaurant\n"
                           "[3] Insert data for multiple restaurants\n"
                           "[4] Go back\n")
    valid = False
    while not valid:
        if user_selection == '1':
            valid = True
            insert_review()
        elif user_selection == '2':
            valid = True
            insert_one()
        elif user_selection == '3':
            valid = True
            insert_many()
        elif user_selection == '4':
            valid = True
        else:
            print("Option not valid.")
            user_selection = input(
                "Enter the data you would like to insert:\n"
                "[1] Insert restaurant review\n"
                "[2] Create/Insert data for one restaurant\n"
                "[3] Create/Insert data for multiple restaurants\n"
                "[4] Go back\n")


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
                rate_reviews = input("Would you like to see the "
                                     "reviews for this restaurant? [Y/N]:")
                if rate_reviews == "Y" or rate_reviews == "y":
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
        print(f'{name} in {borough} serves '
              f'{cuisine}, and it rated {ave_rating}/5')
        if ave_rating is not None:
            rate_reviews = input("Would you like to see the "
                                 "reviews for this resturant? [Y/N]:")
            if rate_reviews == "Y" or rate_reviews == "y":
                for i, rating in enumerate(rating):
                    print(f'{rating}/5. Comments: {comments[i]}')

        input("Enter to exit: ")
    else:
        print("No restaurant found that has that name.")
        input("Enter to exit: ")


def read_data() -> None:
    """Read data from DB"""
    user_selection = input("Enter the data you would like to read:\n"
                           "[1] Reviews from all restaurants\n"
                           "[2] Reviews from one restaurant\n"
                           "[3] Go back\n")
    valid = False
    while not valid:
        if user_selection.isdigit():
            if user_selection == '1':
                valid = True
                read_all()
            elif user_selection == '2':
                valid = True
                read_one()
            elif user_selection == '3':
                valid = True

        print("Option not valid.")
        user_selection = input("Enter the data you would like to read:\n"
                               "[1] Reviews from all restaurants\n"
                               "[2] Reviews from one restaurant\n"
                               "[3] Go back\n")


def update() -> None:
    """update data"""
    name = input("Enter the name of the restaurant you want to edit: ")

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
        print("updated restaurant data.")
        input("Enter to exit: ")
    else:
        print("No restaurants found that match your perameter.")
        input("Enter to exit: ")


def delete() -> None:
    """delete data"""
    name = input("Enter the name of the restaurant you want to delete: ")
    result = collection.delete_many({"name": name})
    print(f'{result.deleted_count} records deleted!')
    input("Enter to exit: ")


def show_menu() -> int:
    """menu for ui"""
    options = """
    [1] Make sure collection is created
    [2] Fill the collection
    [3] Insert a review or data for one or more restaurants
    [4] Read all or one restaurant's data
    [5] update restaurant's data
    [6] delete a restaurant
    [7] exit
    """

    os.system("clear")
    print(options)
    choice = input("Enter option [1-7]: ")

    while True:
        if choice.isdigit():
            if 1 <= int(choice) <= 7:
                return int(choice)
            else:
                os.system("clear")
                print(options)
                choice = input("Enter a valid option[1-7]: ")
        else:
            os.system("clear")
            print(options)
            choice = input("Enter a valid option[1-7]: ")


def main() -> None:
    """Main driver"""
    while True:
        choice = show_menu()
        if choice == 1:
            number_of_documents()
        elif choice == 2:
            fill_table()
        elif choice == 3:
            insert_data()
        elif choice == 4:
            read_data()
        elif choice == 5:
            update()
        elif choice == 6:
            delete()
        elif choice == 7:
            exit(0)


main()
