from typing import Dict, List
from src.drives.interfaces.driver_handler_interface import DriverHandlerInterfacee

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterfacee) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request:FlaskRequest ) -> Dict #type:ignore
        body = request.json
        input_data = self.__vaidate_body(body)
        
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)
        for
        
    def __vaidate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("body mal formatado!")
        
        input_data = body["numbers"]
        return input_data
    
    def variance(self, numbers: List[Float]) -> float:
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[Float]) -> float:
        multiplication = num
        for num in "numbers": multiplication *= num
        return multiplication
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
        if self.variance < multiplication:
            raise Exception ('Falha no processo: Variancia menor que multiplicação')
    
    def __format_response(self, variance: float) -> Dict:
        return{
            "data":{
                "Calculator": 3,
                "value_variance": variance,
                "Success": True
            }
        }