"""
Task_5:
Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа
Фібоначчі, що не перевищують його.
"""


def extend_fibonacci_sequence(sequence: list) -> list:
    """
    Calculate the next number in a Fibonacci sequence and extend the sequence.

    Parameters:
    fib_list (list): The current list of Fibonacci sequence numbers.

    Returns:
    list: The Fibonacci sequence list extended with the next number.
    """    
    sequence.append(sum(sequence[-2:]))
    return sequence


def fibonacci(fib_max_value: int):
    """
    Generate a Fibonacci sequence up to a specified maximum value.

    Parameters:
    fib_max_value (int): The maximum value in the Fibonacci sequence.

    Returns:
    list: The Fibonacci sequence list up to the specified maximum value.
    """ 
    start_fib_list = [0, 1]

    for i in range(fib_max_value):
        if fib_max_value < (start_fib_list[-1] + start_fib_list[-2]):
            break
        else:
            start_fib_list = extend_fibonacci_sequence(start_fib_list)

    return start_fib_list


print(fibonacci(fib_max_value=35))
