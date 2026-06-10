from abc import ABC, abstractmethod
from typing import List

class DriverHandlerInterfacee(ABC):
    
    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass
    
    @abstractmethod
    def variance(self, numvbers: List[float]) ->float:
        pass