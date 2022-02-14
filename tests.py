from contractsPY.decorators import if_fails
from contractsPY.usecase import Usecase

user_repo = None
user_factory = None

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def __repr__(self):
        return f'User(username={self.username}, password={self.password})'


# TODO: Implement proper tests

users = []

test_user = User(username='test', password='test')

users.append(test_user)

# Usecase 1 - Create user

@if_fails(message="not_valid")
def validate_inputs(state):
    if state.password and state.username:
        return True
    return False

@if_fails(message="not_generated")
def generate_user(state):
    state.user = User(state.username, state.password)
    return True if state.user else False

@if_fails(message="user_exists")
def validate_user_exists(state):
    for user in users:
        if user.username == state.user.username:
            return False
    return True

@if_fails(message="not_persisted")
def persist_user(state):
    users.append(state.user)
    return True if state.user else False

register_user = Usecase()
register_user.contract = [
    validate_inputs,
    generate_user,
    validate_user_exists,
    persist_user
]

if  __name__ == '__main__':
    r = register_user.apply(username='test', password='test')
    print(r)
    print(users)