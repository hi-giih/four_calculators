from typing import Dict
from pytest import raises 
from src.drives.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError:#alteração
	def standard_derivation(self, numbers: List[Float]) -> float:
		return 3		

class MockDriverHandler: #altera~]ao
	def standard_derivation(self, numbers: List[Float]) -> float:
		return 100000
        

def teste_caculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1,2,3,4,5]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculator_3.caclulate(mock_request)
	
    assert str(excinfo.value) == 'Falha no processo: Variancia menor que multiplicação'

def teste_calculate():
    mock_request = MockRequest({"numbers": [1,1,1,1,100]})
    calculator_3 = Calculator3(MockDriverHandler())
    
    response = calculator_3.caclulate(mock_request) 
    assert response == {"data":{'Calculator': 3,'value':1568.16, 'Sucess':True}}
    