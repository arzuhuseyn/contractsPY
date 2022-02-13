Python Business Transactions Library - ContractsPY
=======

Declare and define business transactions in Python. Use the contracts library to
validate business transactions with Railway-oriented approach.

TODO: Add more documentation.

 ### Compatibility

Tested on Python 3.8+


**Example (Create User):**

```python
from contractspy import if_fails, UseCase


@if_fails(message="not_valid")
def validate_inputs(state):
    ...
    return True if state.password else False

@if_fails(message="user_exists")
def validate_user_exists(state):
    ...
    return False

@if_fails(message="not_generated")
def generate_user(state):
    ...
    return True

@if_fails(message="not_persisted")
def persist_user(state): # You shoudl set result value in last step
    ...
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

```

**Result:**

```python
>>> Result(value={'password': '123', 'result': 'Great'}, case=success)
```


***(C) Arzu Hussein***
