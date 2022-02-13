from typing import Any

from contractsPY.exceptions import StateException


class State:
    __dict = {}
    
    def __repr__(self) -> str:
        return str(self.__dict)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict[__name] = __value
        
    def __getattr__(self, __name: str) -> Any:
        if self.__dict.get(__name):
            return self.__dict[__name]
        raise StateException(f'{__name} is not set')
    
    def __str__(self) -> str:
        return str(self.__dict)