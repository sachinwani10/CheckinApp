from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be empty"
    )

    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be empty"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "User " + data['username'] + " already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully'}, 201

    # def delete(self):
    #     data = UserRegister.parser.parse_args()
    #     # code to delete user_standard
    #     # only super user should be authorized to delete(handle at front end)
