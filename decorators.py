from result import ResultCase, Result
 
 
def if_fails(message):
    def Inner(func):
        def wrapper(*args, **kwargs):
            try:
                
                if not func(*args, **kwargs):
                    result = Result(func(*args, **kwargs), case=ResultCase.ERROR)
                    result.reason = message
                    return result
                
                return Result(
                    func(*args, **kwargs),
                    case=ResultCase.SUCCESS
                )
            except:
                result = Result(func(*args, **kwargs), case=ResultCase.ERROR)
                result.reason = message
                return result
        return wrapper
    return Inner
