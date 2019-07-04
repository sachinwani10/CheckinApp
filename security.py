from user import User

# here user is created manually
# next step: 1. create user with provided username, password
#            2. create unique id for that users
#            3. store that user into users table(into database)
#            4. stored values will include(id, username, password)

users = { User(1, 'bob', 'asdf')}

# for username_mapping and userid_mapping create two more tables
# instead of using dictionaries
# along with users table, these tables will be updated when new user is created
# you have to figure out how to update these tables when users table is updated
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}

def authenticate(username, password):
    # here we get he user from dictionary with username, then find password
    # when switched to database you can directly extract password from database-
    # by using username
    # then if provided password matches with database password return user as--
    # object (coz i think identity method need user object in the background)
    # right now i dont know if return type for this method has to be an object
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    # on line 33 dictionary is used again
    # use user_id from line 30 to extract password from db and then return it
    return userid_mapping.get(user_id, None)
