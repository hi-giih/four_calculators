from typing import Dict
from flask import request as FlaskRequest

from src.erros.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_date = self.__validate_body(body)
        slited_number = input_date / 3
        
        first_process_result = self.__first_process(slited_number)
        secod_number_result = self.__second_process(slited_number)
        
        calc_result = first_process_result + secod_number_result + slited_number
        
        response = self.__format_response(calc_result)
        return response
        
    
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")
        
        input_data = body["number"]
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number /4) +7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, secod_number: float) -> float:
        first_part = (secod_number ** 2.121)
        secod_number = (first_part / 5) +1
        return secod_number
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result,2)
            }
        }
        
        