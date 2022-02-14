Python Business Transactions Library - ContractsPY
=======

Declare and define business transactions in Python. Use the contracts library to
validate business transactions with Railway-oriented approach.

 ### Compatibility

Tested on Python 3.8+

### Installation

There is no additional dependencies. Library's footprint is small.

```bash
>>> pip install contractsPY
```


### Contract functions

Contract functions are simple python functions that return True or False. They are
used to define business rules for transactions. They accept only one argument,
which is the current state of the transaction.

```python
def my_contract(state):
    return state.a > state.b
```


### Example (Create User):

Let's assume we have a user service that creates a new user. There are multiple steps to create a new user. 

1) First, we need to validate the user's data.
2) Then, we need to make sure that the user doesn't already exist.
3) We need to save the user to the database.
4) We need to send an email to the user.

There are many ways to do this. We can use the contracts library to make it easier and more readable. 
All you need to do is to define a contract for each step. I can hear you saying "Why do I need to make things like this?". Well, I'm glad you asked.

- Railway-oriented approach:

As we mentioned before, the contractsPY library uses the Railway-oriented approach. This approach helps you to handle every possible scenario on the way to the final step. That's why they called it "Railway-oriented". 

Whenever you call a function, there are two possible returns (success and failure). Your business logic is executed in the success case. If the business logic fails, you can handle the failure case.


```python
from contractspy import if_fails, Usecase


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
    result = register_user.apply(username='johndoe', password='foobar')
    print(result)

```

**Result:**

As you can see from the Result, user was not created. The reason is that the user already exists.
Now, we can handle the failure case, and send proper error messages to the user.

```python
>>> Result(state={'username': 'johndoe', 'password': 'foobar', 'user': User(username=johndoe, password=foobar)}, case=error, message=user_exists)
```

The result object contains three fields. State, case, message. You can check the case and message to see what went wrong. If everything went well, you can pick a value from the state dictionary.

```python
result.state = {'username': 'johndoe', 'password': 'foobar', 'user': User(username=johndoe, password=foobar)}

result.case = error

result.message = 'user_exists'
```


If there was no failure, the result should have been like this:

```python
>>> Result(state={'username': 'johndoe', 'password': 'foobar', 'user': User(username=johndoe, password=foobar)}, case=success, message=None)
```


***(C) Arzu Hussein***
