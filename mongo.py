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
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# Call Mongo Connect function
conn = mongo_connect(MONGODB_URI)

# Collection name
coll = conn[DBS_NAME][COLLECTION_NAME]

# Insert new record to the database
new_docs = {'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_color': 'not much', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_color': 'white', 'occupation': 'writer', 'nationality': 'american'}

coll.insert_many(new_docs)

# Print everything that is in the database
documents = coll.find()

for doc in documents:
    print(doc)
