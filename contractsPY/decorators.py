from contractsPY.result import ResultCase, Result
 
 
def if_fails(message):
    def wrapper(func):
        setattr(func, 'message', message)
        return func
    return wrapper
    

def chained(state):
    def wrapper(func):
        
        expected_result = func(state)
        # If message is not set, then message should be a func name
        if hasattr(func, 'message'):
            message = func.message
        else:
            message = func.__name__
            
        try:
            if not expected_result:
                result = Result(state, case=ResultCase.ERROR.value)
                result.message = message
                return result
            
            return Result(
                state,
                case=ResultCase.SUCCESS.value
            )
        except:
            result = Result(state, case=ResultCase.ERROR.value)
            result.message = message
            return result
        
    return wrapper
    