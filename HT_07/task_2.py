"""
Task_2:

Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
   цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із
   відповідним текстом.
"""


import re


class UsernameValidationError(Exception):
    """Exception raised for invalid username format."""


class PasswordValidationError(Exception):
    """Exception raised for invalid password format."""


def usernmae_validation(username: str) -> tuple:
    """
    Validate the format of a username.

    Parameters:
    username (str): The username to be validated.

    Regular expression pattern:
        Username must contain at least 3 characters
        rulle_pattern_01 = r"^.{3,}$"

        Username must not exceed 50 characters
        rulle_pattern_02 = r"^.{1,50}$"

    Returns:
    tuple: A tuple containing two values:
        - validation_result (bool): True if the username is valid, False if it's not.
        - username_verification_steps (dict): A dictionary with validation steps as keys
          and their results (True or False) as values.
    """
    username_verification_steps = {"Username must contain at least 3 characters": False,
                                   "Username must not exceed 50 characters": False,}

    rulle_pattern_01 = r"^.{3,}$"
    rulle_pattern_02 = r"^.{1,50}$"
    
    username_verification_steps['Username must contain at least 3 characters'] = bool(re.match(rulle_pattern_01, username))
    username_verification_steps['Username must not exceed 50 characters'] = bool(re.match(rulle_pattern_02, username))
    
    validation_result = True
    for step in username_verification_steps:
        if username_verification_steps[step] is False:
            validation_result = False
            break

    return (validation_result, username_verification_steps)


def password_validation(password: str) -> tuple:
    """
    Validate the format of a password.

    Parameters:
    password (str): The password to be validated.

    Regular expression pattern:
        Password must contain at least 8 characters
        rulle_pattern_01 = r".{8,}$"

        Password must contain at least one digit
        rulle_pattern_02 = r".*\d+.*"

        Password must contain at least one uppercase letter
        rulle_pattern_03 = r".*[A-Z]+.*"

    Returns:
    tuple: A tuple containing two values:
        - validation_result (bool): True if the password is valid, False if it's not.
        - pass_verification_steps (dict): A dictionary with validation steps as keys
          and their results (True or False) as values.
    """
    pass_verification_steps = {"Password must contain at least 8 characters": False,
                              "Password must contain at least one digit": False,
                              "Password must contain at least one uppercase letter": False}

    rulle_pattern_01 = r".{8,}$"
    rulle_pattern_02 = r".*\d+.*"
    rulle_pattern_03 = r".*[A-Z]+.*"

    pass_verification_steps['Password must contain at least 8 characters'] = bool(re.match(rulle_pattern_01, password))
    pass_verification_steps['Password must contain at least one digit'] = bool(re.match(rulle_pattern_02, password))
    pass_verification_steps['Password must contain at least one uppercase letter'] = bool(re.match(rulle_pattern_03, password))

    validation_result = True
    for step in pass_verification_steps:
        if pass_verification_steps[step] is False:
            validation_result = False
            break

    return (validation_result, pass_verification_steps)


def user_validate(username: str, password: str) -> tuple:
    """
    Validate a username and password.

    Parameters:
    username (str): The username to be validated.
    password (str): The password to be validated.

    Returns:
    tuple: A tuple containing the validation result for username and password.
    """
    username_validation_result = usernmae_validation(username)
    password_validation_result = password_validation(password)

    try:
        if username_validation_result[0] is False:
            raise UsernameValidationError("Username error validation!")
    except UsernameValidationError as text_error:
        print(f"Error, detail: {text_error}")
        return [x for x in username_validation_result[1] if username_validation_result[1][x] is False]

    try:
        if password_validation_result[0] is False:
            raise PasswordValidationError("Password error validation!")
    except PasswordValidationError as text_error:
        print(f"Error, detail: {text_error}")
        return [x for x in password_validation_result[1] if password_validation_result[1][x] is False]

    return (username_validation_result[0], password_validation_result[0])


print(user_validate(username="user", password="Somepassword1"))
