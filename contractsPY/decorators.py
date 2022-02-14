from contractsPY.result import ResultCase, Result
 
 
def if_fails(message):
    def wrapper(func):
        setattr(func, 'message', message)
        return func
    return wrapper
    

def chained(state):
    def wrapper(func):
        try:
            expected_result = func(state)
            if not expected_result:
                result = Result(state, case=ResultCase.ERROR)
                result.message = expected_result.message
                return result
            
            return Result(
                state,
                case=ResultCase.SUCCESS
            )
        except:
            result = Result(state, case=ResultCase.ERROR)
            result.message = func.message
            return result
    return wrapper
    