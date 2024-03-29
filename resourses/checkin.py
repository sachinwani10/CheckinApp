from flask_restful import Resource, reqparse
from models.session_sheet import SessionModel
from datetime import datetime
from models.user import UserModel
from flask_jwt import jwt_required

class Checkin(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True)
    parser.add_argument('timestamp_in', type=str, required=True)

    # @jwt_required()
    def post(self):
        data = Checkin.parser.parse_args()
        _timestamp = datetime.strptime(data['timestamp_in'], '%Y-%d-%m %H:%M:%S.%f')
        record = SessionModel(data['username'], _timestamp, None)
        try:
            record.save_checkin()
        except:
            return {"message": data['username'] + " User does not exist"}
        return {"message": "checked in at " + data['timestamp_in']}
