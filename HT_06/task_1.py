"""
Task_1:
Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата
та його діагональ. 
"""


def get_perimete_square(square_side: int) -> int:
    """
    Calculate the perimeter of a square.
    
    Parameters:
    side (int): The length of one side of the square.
    
    Returns:
    int: The perimeter of the square, calculated as 4 times the side length.
    """
    result = square_side * 4
    return result


def get_area_square(square_side: int) -> int:
    """
    Calculate the area of a square.
    
    Parameters:
    side (int): The length of one side of the square.
    
    Returns:
    int: The area of the square, calculated as the square of the side length.
    """
    result = square_side ** 2
    return result


def get_diagonal_square(square_side: int) -> float:
    """
    Calculate the diagonal of a square given the length of one side.
        Parameters:
        square_side (int): The length of one side of the square.
        Returns:
        float: The diagonal of the square, rounded to 2 decimal places.
    """
    result = round(square_side * (2 ** 0.5), 2)
    return result


def square(square_side: int) -> tuple:
    """
    Calculate various properties of a square given the length of one side.

    This function takes one argument, 'square_side', which represents the
    length of one side of the square.
    It calculates and returns a tuple containing three values:
    1. The perimeter of the square.
    2. The area of the square.
    3. The diagonal of the square.

    Parameters:
    square_side (int): The length of one side of the square.

    Returns:
    tuple: A tuple containing the perimeter, area, and diagonal of the square.
    """
    result = (get_perimete_square(square_side),
              get_area_square(square_side),
              get_diagonal_square(square_side),)
    return result


try:
    user_input = int(input("Please enter a side of square: "))
    if user_input < 0:
        raise ValueError("Side length must be a positive number.")
except ValueError as text_error:
    print(f"Error! Details: {text_error}")
else:
    print(f"\nResult: (square perimeter), (square area), (square diagonal):")
    print(square(user_input))
