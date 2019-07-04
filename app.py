from flask import Flask
from flask_restful import Resource, Api
# from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
# app.secret_key = 'sachin'
api = Api(app)

# jwt = JWT(app, authenticate, identity)  # /auth

class Clerk(Resource):
    # @jwt_required()
    def get(self, username):
        # from table username get all the records and return it to front end
        return {'message': 'this is ' + username}

    def get(self, username, startdate, enddate):
        # returned total hours worked for specific amount of period
        pass

    def post(self, username, checkin_date, checkin_time):
        # put the checkin_date and time into database
        # table name is username
        return {'message': 'this is post method'}

    def post(self, username, checkout_date, checkout_time):
        # put the checkout_date and checkout_time into database
        # table name is username
        return {'message': 'this is post method'}


api.add_resource(Clerk, '/clerk/<string:username>')

app.run(debug=True)

# for now lets learn seqlite and then put user tabels manually so that--
# i can write and test above methods.

# also you really need to create multiple files for seperating concerns.
# this can wait till you find out how.
