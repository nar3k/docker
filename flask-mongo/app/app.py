import pymongo
import datetime
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('mongodb', 27017)

db = client.SCtools


scans = db.Scans

import pprint
pprint.pprint(scans.find_one())

scan = { "ip":3232236598, \
"status":"Done", \
"Scanner":"BiZone WannaCry", \
"Result":"OK", \
"Output":"dude" }
scans.insert_one(scan)
