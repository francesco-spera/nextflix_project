from flask_pymongo import PyMongo
from flask import Flask

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Nunzia:freanat8@pythoncluster.ldlif.mongodb.net/quickstart?authSource=admin&replicaSet=atlas-d5hj2e-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
mongo = PyMongo(app)

def connection_pool():
	netflix = mongo.db.netflix
	return netflix		
