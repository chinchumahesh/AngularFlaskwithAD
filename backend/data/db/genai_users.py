import json 
def get_users(genaidb):
    collection = genaidb['g_users'] 
    docs=collection.find({})

    for x in docs:
      print(x)
    return docs


def add_user(genaidb,user_data):
    collection = genaidb['g_users'] 
    print(">>>>>",user_data)
    user = collection.insert_one( { "name": "John", "address": "Highway 37" })
    print(user)
    return user