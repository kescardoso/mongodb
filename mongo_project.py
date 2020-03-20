import pymongo
import os
# Environment Variables
from os import path
if path.exists("env.py"):
    import env


# Constants from pymongo
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


# "Mongo Connect" function string
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# Create CRUD Menu
def show_menu():
    # Blank line for space
    print("")
    # CRUD Menu Options
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    # Variable: option to be selected by user
    option = input("Enter option: ")
    return option

# While Loop: Calls the menu each time user comes back to it
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")

# Create and call connection function and collection object
# Call function
conn = mongo_connect(MONGODB_URI)


# Collection name
coll = conn[DBS_NAME][COLLECTION_NAME]

# Call continuing loop
main_loop()