from models.time_sheet import TimeSheetModel as TS
from flask_restful import Resource

class TotalHours(Resource):
    def get(self, username):
        res = []
        result = TS.find_in_db(username)
        if result:
            for row in result:
                res.append(row.json())
            return {"result": res}
        message = {"None": "None"}
        return message
