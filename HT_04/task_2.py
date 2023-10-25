"""
Task_2:
Create a custom exception class called NegativeValueError. Write a Python
program that takes an integer as input and raises the NegativeValueError
if the input is negative. Handle this custom exception with a try/except
block and display an error message.
"""


class NegativeValueError(Exception):
    """ Negative number value exception """


user_input = int(input("Please enter an integer: "))

try:
    if user_input < 0:
        raise NegativeValueError("Custom Error: 'NegativeValueError' - Integer is negative!")

except NegativeValueError as text_error:
    print(f"Error in the program, details: {text_error}")

else:
    print(f"Your integer: {user_input} is positive number.")
