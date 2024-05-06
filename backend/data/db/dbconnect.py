from pymongo import MongoClient

#C:\Users\chinc\AppData\Local\Programs\mongosh
#C:\Program Files\MongoDB\Server\7.0\bin

#db.createUser(
#   {
#     user: "genaiuser",
#     pwd: "genaipass",
#     roles: [ "dbOwner" ]
#   }
#)
    
def get_db():
    uri = "mongodb://genaiuser:genaipass@localhost:27017/?authSource=genai"
    client = MongoClient(uri)
    genaidb = client["genai"]
    return genaidb


def get_users(genaidb):
    collection = genaidb['g_users'] 
    docs=collection.find({})

    for x in docs:
      print(x)
    return docs
    
def get_users(genaidb):
    collection = genaidb['g_users'] 
    docs=collection.find({})

    for x in docs:
      print(x)
    return docs