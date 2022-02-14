from typing import Any

from contractsPY.decorators import chained
from contractsPY.state import State
from contractsPY.result import Result, ResultCase
from contractsPY.exceptions import StateException, ContractException


class Usecase:
    """
        Main class for usecase.
        
        Main methods:
            contract - list of functions that will be executed in order
            apply - execute contract functions
    """
    __state = State()
    __contract = []
    
    @property
    def state(self) -> State:
        return self.__state
    
    @state.setter
    def state(self, values: dict) -> None:
        
        if not isinstance(values, dict):
            raise Exception('State must be a dict')
        
        for k, v in values.items():
            setattr(self.__state, k, v)
        
    @property
    def contract(self) -> list:
        return self.__contract
    
    @contract.setter
    def contract(self, funcs: list) -> None:
        
        if not funcs:
            raise ContractException('Contract cannot be empty')
        
        if len(self.contract) > 0:
            raise ContractException('Contract cannot be changed')
        
        if not isinstance(funcs, list):
            raise ContractException('Contract must be a list')
        
        for func in funcs:
            
            if not callable(func):
                raise ContractException('Contract must be a list of callables')
            
            self.__contract.append(func)
    
    def apply(self, **kwargs) -> Result:
        self.state = kwargs
        
        for func in self.contract:
           
            result = chained(self.state)(func)
            if not result.is_success():
                return result
                
        return Result(self.state, ResultCase.SUCCESS.value)