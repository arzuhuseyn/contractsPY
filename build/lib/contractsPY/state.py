from typing import Any, Dict

from contractsPY.exceptions import StateException


class State(dict):
    __dict: Dict[str, Any] = {}
    
    def __repr__(self) -> str:
        return str(self.__dict)
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        self.__dict[__name] = __value
        
    def __getattr__(self, __name: str) -> Any:
        if __name in self.__dict:
            return self.__dict[__name]
        raise StateException(f'{__name} is not set')
    
    def get(self, __name):
        return self.__dict.get(__name, None)
    
    def __str__(self) -> str:
        return str(self.__dict)