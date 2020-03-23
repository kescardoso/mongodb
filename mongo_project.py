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


# Helper function (reusable) to assist on find, update and delete functions
def get_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")

    try:
        # Calling the lower method on first and last name
        # which will be stored in lower case
        doc = coll.find_one({'first': first.lower(), 'last': last.lower()})
    except:
        print("Error accessing the database")

    # In case document-object is empty
    if not doc:
        print("")
        print("Error! No results found.")
    
    return doc


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

    # Variable: options to be selected by user
    option = input("Enter option: ")
    return option


# Input where user can enter new record information to the database
# using the option from the CRUD Menu
def add_record():
    print("")
    first = input ("Enter first name > ")
    last = input ("Enter last name > ")
    dob = input ("Enter date of birth > ")
    gender = input ("Enter gender > ")
    hair_colour = input ("Enter hair colour > ")
    occupation = input ("Enter occupation > ")
    nationality = input ("Enter nationality > ")

    # Dictionary (string) to be inserted into the database
    # Variable names and their keys
    # Calling the lower method on first and last name
    new_doc = {'first': first.lower(), 'last': last.lower(), 'dob': dob, 'gender': gender, 'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}

    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


# Find function
def find_record():
    doc = get_record()
    if doc:
        print("")
        # k = keys , v = values
        for k,v in doc.items():
            if k!= "_id":
                print(k.capitalize() + ":  " + v.capitalize())


# While Loop: Calls the menu each time user comes back to it
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
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
