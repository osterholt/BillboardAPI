from pymongo import MongoClient

client = MongoClient('mongodb+srv://camo:qMPMo53!9X*B@billboardapi.ww9aumm.mongodb.net/')
db = client["BillboardAPI"]
collection = db["bb_csv"]
