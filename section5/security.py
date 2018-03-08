from werkzeug.security import safe_str_cmp
from user import User

#deleted previous static list object since now using sqlite database.

def authenticate(username, password):
    #user = username_mapping.get(username, None)
    user = User.find_by_username(username)
    #dictionary.get method, sets default to None if key requested is absent.
    #if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        #safe_str_cmp handles different string encodings safely.
        #jwt token returned
        return user
    #return {"message": "no user found in security.authenticate"}

def identity(payload):
    userid = payload['identity']
    #return userid_mapping.get(userid, None)
    return User.find_by_id(userid)
