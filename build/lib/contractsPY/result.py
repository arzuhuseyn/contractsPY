from enum import Enum
from typing import Any


class ResultCase(Enum):
    SUCCESS = 'success'
    ERROR = 'error'
    FAILURE = 'failure'


class Result(object):
    __slots__ = ('state', 'case', 'message')
    
    def __init__(self, state: dict, case: str) -> None:
        self.state = state
        self.case = case
        self.message = "OK"
        
    def __repr__(self) -> str:
        return f'Result(state={self.state}, case={self.case}, message={self.message})'
    
    def set_message(self, message: str) -> None:
        self.message = message
    
    def is_success(self) -> bool:
        return self.case == ResultCase.SUCCESS.value
    
    def is_failed(self) -> bool:
        return self.case == ResultCase.ERROR.value
    
    def is_crashed(self) -> bool:
        return self.case == ResultCase.FAILURE.value
    
    @property
    def failure_reason(self):
        if self.is_failed():
            return self.message