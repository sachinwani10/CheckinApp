from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from clerk import Clerk, ClerkTotalHours

app = Flask(__name__)
app.secret_key = 'sachin'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Clerk, '/clerk/<string:username>')
api.add_resource(ClerkTotalHours, '/hours/<string:username>/<string:startDate>/<string:endDate>')
api.add_resource(UserRegister, '/register')

app.run(debug=True)

# multiple POST or GET cant be written therefore i have to do operations based
# on what i am receiving.
# to distinguish between what i am receiving i can use a flag which will denote
# 1. For POST - if date and time received are checkin our checkOut
# 2. for GET - Just return table data for now and figure out how you can use
#              URL encoding to get record only from provided time period
#              as well as you can also return total hours worked for that period
