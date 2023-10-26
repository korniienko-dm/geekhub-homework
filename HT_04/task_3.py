"""
Task_3:
Create a Python script that takes an age as input. If the age is less than
18 or greater than 120, raise a custom exception called InvalidAgeError.
Handle the InvalidAgeError by displaying an appropriate error message.
"""


class InvalidAgeError(Exception):
    """ Invalid age value exception """


user_input = int(input("Please enter a your age (positive integer): "))

try:
    if user_input not in range(18, 121):
        raise InvalidAgeError("Custom Error: 'InvalidAgeError' - Value is not correct.")

except InvalidAgeError as text_error:
    print(f"Error in the program, details: {text_error}")

else:
    print(f"{user_input} - is valid age! Value accepted.")
