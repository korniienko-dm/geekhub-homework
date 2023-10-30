"""
Task_5:
Ну і традиційно - калькулятор :slightly_smiling_face: Повинна бути 1 ф-цiя,
яка б приймала 3 аргументи - один з яких операцiя, яку зробити! Аргументи
брати від юзера (можна по одному - 2, окремо +, окремо 2; можна всі
разом - типу 1 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **.
Не забудьте протестувати з різними значеннями на предмет помилок!
"""


def calculate_expression(first_operand: int, second_operand: int, math_operation: str):
    """
    This function processes two numbers and applies a mathematical operation to them.

    Supported mathematical operations:
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    - Modulus (%)
    - Floor Division (//)
    - Exponentiation (**)

    Returns a string with the result of the expression if a valid operation is entered, 
    otherwise returns "Invalid math operation entered."
    """

    math_operator_collection = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
        "%": lambda x, y: x % y,
        "//": lambda x, y: x // y,
        "**": lambda x, y: x ** y,
    }

    if math_operation in math_operator_collection:
        try:
            result_math_operation = math_operator_collection[math_operation](
                first_operand, second_operand)
        except Exception as text_error:
            return f'Error! Details: {text_error}'
        else:
            return f"Result your expression: {first_operand} {math_operation} {second_operand} = {result_math_operation}"

    else:
        return "Invalid math operation entered."


try:
    first_operand = int(input("Plese enter a first number:\n"))
    second_operand = int(input("Plese enter a second number:\n"))
except Exception as text_error:
    print(f'Error! Details: {text_error}')
else:
    math_operation = input('Enter a math operation\n(" +", "-", "*", "/", "%", "//", "**"):\n')

try:
    print(calculate_expression(first_operand, second_operand, math_operation))
except NameError as text_error:
    print(f'Error! Details: {text_error}')
