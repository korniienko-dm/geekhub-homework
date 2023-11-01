"""
Task_4:
Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець
діапазона, і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку
невідповідності - виведіть повідомлення.
"""


def is_prime(number):
    """
    Check if a number is prime.

    This function determines whether a given number is a prime number or not.

    Parameters:
    number (int): The number to be checked for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """    
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


def prime_list(start_range:int, end_range:int) -> list:
    """
    Generate a list of prime numbers within the specified range.

    This function calculates and returns a list of prime numbers in the given range
    from 'start_range' (inclusive) to 'end_range' (inclusive).

    Parameters:
    start_range (int): The starting value of the range (inclusive).
    end_range (int): The ending value of the range (inclusive).

    Returns:
    list: A list of prime numbers within the specified range.
    str: An error message if 'start_range' is greater than 'end_range'.
    """    
    list_of_prime_number = list()

    try:
        if start_range > end_range:
            raise ValueError("The start of the range cannot be bigger than the end of the range.")
    
    except ValueError as text_error:
        return f"ValueError - {text_error}"
    
    else:
        for i in range(start_range, end_range + 1):
            if is_prime(i):
                list_of_prime_number.append(i)
        
        return list_of_prime_number


try:
    start_range = int(input('Please enter a "start range" value: '))
    end_range =  int(input('Please enter a "end range" value: '))
except Exception as text_error:
    print(f"Error! Details: {text_error}")
else:
    print(prime_list(start_range, end_range))