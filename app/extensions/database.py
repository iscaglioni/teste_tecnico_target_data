from pymongo import MongoClient

# criando conexao com pymongo
def database():
    CONNECTION_STRING = 'mongodb://localhost:27017'
    client = MongoClient(CONNECTION_STRING)
    return client['db_target_data']