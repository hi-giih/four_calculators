from src.calculators.calculator_1 import Calculator1 

def calculator_1_factory():
    calc = Calculator1()
    response = calc.calculate(request)
    return jsonify(response),200