# https://stackoverflow.com/questions/26662702/what-is-the-datetime-format-for-flask-restful-parser
from flask_restful import Resource, reqparse
from models.session_sheet import SessionModel
from datetime import datetime

class Checkin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True)
    parser.add_argument('timestamp_in', type=str, required=True)

    def post(self):
        data = Checkin.parser.parse_args()
        _timestamp = datetime.strptime(data['timestamp_in'], '%Y-%d-%m %H:%M:%S.%f')
        record = SessionModel(data['username'], _timestamp, None)
        record.save_checkin()
        return {"message": "checked in at " + data['timestamp_in']}
