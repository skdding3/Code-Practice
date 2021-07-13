### MONGO DB

import csv
import os
from pymongo import MongoClient

host = 'host_name'
user = 'user_name'
password = 'password'
database_name = 'myFirstDatabase'
collection_name = 'segment'

MONGO_URI = f"mongodb+srv://{user}:{password}@{host}/{database_name}?retryWrites=true&w=majority"

connection = MongoClient(MONGO_URI)
db = connection.myFirstDatabase