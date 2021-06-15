import pymongo

def connection_pool():
	client = pymongo.MongoClient("mongodb+srv://Nunzia:freanat8@pythoncluster.ldlif.mongodb.net/quickstart?authSource=admin&replicaSet=atlas-d5hj2e-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")
	return client.db.netflix