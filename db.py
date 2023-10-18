
from pymongo.mongo_client import MongoClient
from bson import json_util
import json


uri = "mongodb+srv://yellowflashlight4:admin123@cluster0.0bne9ua.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.chatbot
    collection = db.botquery

except Exception as e:
    print(e)

def load_database():
    print("loading json on MongoDB...")
    json_file_path = "intents.json"

    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    filter = {"_id":"652b8dcfd2f1cd3aa5fb82cf"} 
    update = {"$set": json_data}  
    collection.update_one(filter, update, upsert=True)

def read_database():
    cursor = collection.find()
    data_to_store = list(cursor)
    data_to_store=data_to_store[0]
    json_file_path = "intents.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(data_to_store, json_file, default=json_util.default, indent=2)


read_database()
