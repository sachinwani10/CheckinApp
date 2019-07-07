from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resourses.user import UserRegister
from resourses.checkin import Checkin
from resourses.checkout import Checkout
from resourses.totalhours import TotalHours
# from resourses.clerk import Clerk, ClerkTotalHours

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user_standard:sourcecode10@127.0.0.1:3306/checkindb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sachin'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Checkin, '/checkin') # POST (Body: username, timestamp_in)
api.add_resource(Checkout, '/checkout') # POST (Body: username, timestamp_out)
api.add_resource(TotalHours, '/totalhours/<string:username>') # GET
api.add_resource(UserRegister, '/register')
# api.add_resource(Clerk, '/clerk/<string:username>')
# api.add_resource(ClerkTotalHours, '/hours/<string:username>/<string:startDate>/<string:endDate>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)
