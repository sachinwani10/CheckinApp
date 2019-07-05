from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resourses.user import UserRegister
from resourses.clerk import Clerk, ClerkTotalHours

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sachin'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth

api.add_resource(Clerk, '/clerk/<string:username>')
api.add_resource(ClerkTotalHours, '/hours/<string:username>/<string:startDate>/<string:endDate>')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

# Next Steps:
# 3. Create database Model in models packages
# 4. Write resourse methods
