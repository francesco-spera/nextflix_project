import pymongo

def connection_pool():
	client = pymongo.MongoClient('mongodb://localhost:27017/')
	netflix = client['netflix']['netflix']
	return netflix
