from flask_restful import Resource, reqparse
from models.session_sheet import SessionModel
from datetime import datetime

class Checkout(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('username', type=str, required=True)
    parser.add_argument('timestamp_out', type=str, required=True)

    def post(self):
        data = Checkout.parser.parse_args()
        _timestamp = datetime.strptime(data['timestamp_out'], '%Y-%d-%m %H:%M:%S.%f')
        record = SessionModel(data['username'], None, _timestamp)
        record.save_checkout()
        return {"message": "checked out at " + data['timestamp_out']}
