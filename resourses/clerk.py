from flask import Flask, request
from flask_restful import Resource
from flask_jwt import jwt_required
from models.time_sheet import TimeSheetModel as TS

class Clerk(Resource):
    # @jwt_required()
    def get(self, username):
        res = []
        result = TS.find_in_db(username)
        if result:
            for row in result:
                res.append(row.json())
            return {"result": res}
        message = {"None": "None"}
        return message

    def post(self, username):
        data = request.get_json()
        record = TS(data['date'], data['day'], username, data['timee'])
        record.save_to_db()
        # possible values for action = "checkin/checkout"
        # TS.save_to_db(data['date'], data['day'], username, data['timee'] )
        return {"message": "updated"}


class ClerkTotalHours(Resource):
    # @jwt_required()
    def get(self, username, startDate, endDate):
        # return total hours worked for a period
        return {"user": username,
                "startDate": startDate,
                "endDate": endDate
        }
