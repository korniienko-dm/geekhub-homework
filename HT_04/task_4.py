"""
Task_4:
Write a Python program that demonstrates exception chaining. Create a
custom exception class called CustomError and another called SpecificError.
In your program (could contain any logic you want), raise a SpecificError,
and then catch it in a try/except block, re-raise it as a CustomError with
the original exception as the cause. Display both the custom error message
and the original exception message.
"""


class CustomError(Exception):
    """ Custom exception """


class SpecificError(Exception):
    """  Specific exception """


python_is_cool = False

try:
    if python_is_cool == False:
        raise SpecificError("Error - Wrong meaning about cool.")

except SpecificError as text_error:
    raise CustomError("Python is cool!") from text_error
