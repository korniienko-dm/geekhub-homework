"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи
повинні виконувати математичні операції з 2-ма числами, а саме додавання,
віднімання, множення, ділення.
- Якщо під час створення екземпляру класу звернутися до атребута last_result
  він повинен повернути пусте значення.
- Якщо використати один з методів - last_result повенен повернути результат
  виконання ПОПЕРЕДНЬОГО методу.
    Example:

    last_result --> None 
    1 + 1
    last_result --> None
    2 * 3
    last_result --> 2
    3 * 4
    last_result --> 6
    ...

- Додати документування в клас (можете почитати цю статтю:
https://realpython.com/documenting-python-code/ )
"""

class Calc:
    """
    A simple calculator class.

    This class provides basic mathematical operations such as addition,
    subtraction, multiplication, and division. It also keeps track of the
    last and previous results.

    Attributes:
    - last_result (float or None): The result of the last operation.
    - previous_result (float or None): The result of the previous operation.
    """ 

    def __init__(self):
        """
        Initialize a new Calculator object.

        The calculator is initialized with `last_result` and `previous_result`
        set to None.
        """        
        self.last_result = None
        self.previous_result = None


    def add(self, first_number, second_number):
        """
        Add two numbers.

        Args:
        - first_number (float): The first number.
        - second_number (float): The second number.

        Returns:
        float: The result of the addition.
        """
        result = first_number + second_number
        self.last_result = self.previous_result
        self.previous_result = result
        return result


    def subtract(self, first_number, second_number):
        """
        Subtract one number from another.

        Args:
        - first_number (float): The number to subtract from.
        - second_number (float): The number to subtract.

        Returns:
        float: The result of the subtraction.
        """        
        result = first_number - second_number
        self.last_result = self.previous_result
        self.previous_result = result
        return result
    

    def multiply(self, first_number, second_number):
        """
        Multiply two numbers.

        Args:
        - first_number (float): The first number.
        - second_number (float): The second number.

        Returns:
        float: The result of the multiplication.
        """        
        result = first_number * second_number
        self.last_result = self.previous_result
        self.previous_result = result
        return result

    def divide(self, first_number, second_number):
        """
        Divide one number by another.

        Args:
        - first_number (float): The number to be divided.
        - second_number (float): The divisor (should not be zero).

        Returns:
        float or None: The result of the division, or None if division by zero.
        """        
        if second_number != 0:
            result = first_number / second_number
            self.last_result = self.previous_result
            self.previous_result = result
            return result
        else:
            self.last_result = self.previous_result
            self.previous_result = None
            return None


my_calc = Calc()
print(my_calc.last_result)

my_calc.add(1, 1)
print(my_calc.last_result)

my_calc.multiply(2, 3)
print(my_calc.last_result)

my_calc.multiply(3, 4)
print(my_calc.last_result)
