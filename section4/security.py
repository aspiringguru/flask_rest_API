from werkzeug.security import safe_str_cmp
from user import User
users = [    User(1, 'bob', 'asdf') ]

username_mapping = { u.username: u for u in users }
userid_mapping = { u.id: u for u in users }



def authenticate(username, password):
    user = username_mapping.get(username, None)
    #dictionary.get method, sets default to None if key requested is absent.
    #if user and user.password == password:
    if user and safe_str_cmp(user.password, password):
        #safe_str_cmp handles different string encodings safely.
        return user

def identity(payload):
    userid = payload['identity']
    return userid_mapping.get(userid, None)
