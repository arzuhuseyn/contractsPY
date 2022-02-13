from decorators import if_fails
from usecase import Usecase

user_repo = None
user_factory = None


# TODO: Implement proper tests


# Usecase 1 - Create user

@if_fails(message="not_valid")
def validate_inputs(state):
    if state.password:
        return True
    raise ValueError("Password is not valid")

@if_fails(message="user_exists")
def validate_user_exists(state):
    return True

@if_fails(message="not_generated")
def generate_user(state):
    return True

@if_fails(message="not_persisted")
def persist_user(state):
    state.result = 'Great'
    return True if state.result else False

register_user = Usecase()
register_user.contract = [
    validate_inputs,
    validate_user_exists,
    generate_user,
    persist_user
]

if  __name__ == '__main__':
    r = register_user.apply(password='123')
    if r.is_success():
        print(r)