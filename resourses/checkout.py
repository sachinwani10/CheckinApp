from flask_restful import Resource, reqparse
from models.session_sheet import SessionModel
from datetime import datetime
from models.user import UserModel
from flask_jwt import jwt_required

class Checkout(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True)
    parser.add_argument('timestamp_out', type=str, required=True)

    # @jwt_required()
    def post(self):
        data = Checkout.parser.parse_args()
        _timestamp = datetime.strptime(data['timestamp_out'], '%Y-%d-%m %H:%M:%S.%f')
        record = SessionModel(data['username'], None, _timestamp)
        try:
            record.save_checkout()
        except:
            return {"message": data['username'] + " User does not exist"}
        return {"message": "checked out at " + data['timestamp_out']}
