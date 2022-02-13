from enum import Enum
from typing import Any


class ResultCase:
    SUCCESS = 'success'
    ERROR = 'error'


class Result(object):
    __slots__ = ('value', 'case', 'reason')
    
    def __init__(self, value: dict, case: str) -> None:
        self.value = value
        self.case = case
        self.reason = None
        
    def __repr__(self) -> str:
        if self.case == ResultCase.SUCCESS:
            return f'Result(value={self.value}, case={self.case})'
        return f'Result(value={self.value}, case={self.case}, reason={self.reason})'
    
    def is_success(self) -> bool:
        return self.case == ResultCase.SUCCESS
    
    def is_failed(self) -> bool:
        return self.case == ResultCase.ERROR
    
    def get_result(self) -> Any:
        if not self.value.result:
            raise Exception('Result is not valid')
        return self.value.result