from flask import Flask, request
from flask_restful import Resource
from flask_jwt import jwt_required

class Clerk(Resource):
    # @jwt_required()
    def get(self, username):
        # return all records for this user
        return {'message': 'this is ' + username}

    def post(self, username):
        data = request.get_json()
        # possible values for action = "checkin/checkout"
        return {'message': data['action'] + '-' + 'date|time: ' + data['date'] + '|' + data['time'] }


class ClerkTotalHours(Resource):
    # @jwt_required()
    def get(self, username, startDate, endDate):
        # return total hours worked for a period
        return {"user": username,
                "startDate": startDate,
                "endDate": endDate
        }
