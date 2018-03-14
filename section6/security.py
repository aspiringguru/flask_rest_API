from werkzeug.security import safe_str_cmp
from models.user import UserModel
import sys

def authenticate(username, password):
    print('security.authenticate: This error output', file=sys.stderr)
    #print('security.authenticate: This standard output', file=sys.stdout)
    user = UserModel.find_by_username(username)
    if user:
        print('user exists', file=sys.stderr)
    if user and safe_str_cmp(user.password, password):
        print('user exists & password matches', file=sys.stderr)
        return user
    else:
        print('user exists but password mismatch', file=sys.stderr)


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
