from enum import Enum
from typing import Any


class ResultCase:
    SUCCESS = 'success'
    ERROR = 'error'


class Result(object):
    __slots__ = ('state', 'case', 'message')
    
    def __init__(self, state: dict, case: str) -> None:
        self.state = state
        self.case = case
        self.message = None
        
    def __repr__(self) -> str:
        return f'Result(state={self.state}, case={self.case}, message={self.message})'
    
    def is_success(self) -> bool:
        return self.case == ResultCase.SUCCESS
    
    def is_failed(self) -> bool:
        return self.case == ResultCase.ERROR
    
    @property
    def failure_reason(self):
        if self.is_failed():
            return self.message