# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import requests
from data.db import dbconnect,genai_users
from werkzeug.local import LocalProxy
from utils import logger
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app, support_credentials=True)

genaidb = LocalProxy(dbconnect.get_db)
 

@app.route('/rule')
@cross_origin(origin='*')
@logger.timeis
def get_user_profile():
    auth_header = request.headers.get('Authorization')
    endpoint = "https://graph.microsoft.com/v1.0/me"
    data = {}
    headers = {"Authorization": auth_header}
    response = requests.get(endpoint, data=data, headers=headers).json()
    #genai_users.add_user(genaidb, response)
    return response
 

if __name__ == '__main__':
    app.run()