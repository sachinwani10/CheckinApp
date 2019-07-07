# https://stackoverflow.com/questions/26662702/what-is-the-datetime-format-for-flask-restful-parser
from flask_restful import Resource, reqparse
from session_sheet import SessionModel

class Checkin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True)
    parser.add_argument('timestamp_in', type=str, required=True)

    def post(self):
        data = Checkin.parser.parse_args()
        record = SessionModel(data['username'], data['timestamp_in'], None)
        record.save_checkin()
        return {"message": "checked in at " + data['timestamp_in']}
