"""
Task_3:
Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні.
"""


def is_prime(number):
    """
    Check if a number is prime.

    This function determines whether a given number is a prime number or not.

    Parameters:
    number (int): The number to be checked for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    str: An error message if the number is out of range (1 to 1000).
    """    
    try:
        if number > 1000:
            raise ValueError
    except ValueError as text_eror:
        return f"Error: function 'is_prime' accepts values from 1 to 1000"
    else:
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True


print(is_prime(5))
