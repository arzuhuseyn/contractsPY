from typing import Any, Dict

from contractsPY.exceptions import StateException


class State(dict):
    __dict: Dict[str, Any] = {}
    
    def __repr__(self) -> str:
        return str(self.__dict)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if self.__dict.get(__name):
            raise StateException(f'{__name} is already set. You can not set same variable twice.')
        self.__dict[__name] = __value
        
    def __getattr__(self, __name: str) -> Any:
        if self.__dict.get(__name):
            return self.__dict[__name]
        raise StateException(f'{__name} is not set')
    
    def __str__(self) -> str:
        return str(self.__dict)