import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterfacee

class NumpyHandler(DriverHandlerInterfacee):
    def __init__(self) -> None:
        self.__np = numpy
        
    def standard_derivation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    def varience(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)