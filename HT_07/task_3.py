"""
Task_3:
На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь
   по правилам своєї функції) - як валідні, так і ні;

   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором,
   перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення,
   наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
"""


import re


class UsernameValidationError(Exception):
    """Exception raised for invalid username format."""


class PasswordValidationError(Exception):
    """Exception raised for invalid password format."""


username_and_password_data = {'na': 'mypaSS123',
                              'username002': 'Password',
                              'username003': 'password1',
                              'usernmae004': 'Mypass32332',
                              'firstname': 'psPS001abc',
                              'nameUser01': 'vordPASS022',
                              'aa': 'AAgfrfdret',
                              'usernmae': 'sOmePassword',
                              'usrINsytem': '12ZHGsometext',
                              'usernmae001': 'abc',}


def usernmae_validation(username: str) -> tuple:
    """
    Validate the format of a username.

    Parameters:
    username (str): The username to be validated.

    Regular expression pattern:
    ^ - Start of the string.
    [A-Za-z0-9_] - Matches any uppercase letter, lowercase letter, digit, or underscore.
    {3,50} - Specifies the allowed length of the username, between 3 and 50 characters.
    $ - End of the string.

    Returns:
    bool: True if the username is valid, False otherwise.
    """
    username_verification_steps = {"Username must contain at least 3 characters": False,
                                   "Username must not exceed 50 characters": False,}
    # Username must contain at least 3 characters
    rulle_pattern_01 = r"^.{3,}$"
    # Username must not exceed 50 characters
    rulle_pattern_02 = r"^.{1,50}$"
    
    username_verification_steps['Username must contain at least 3 characters'] = bool(re.match(rulle_pattern_01, username))
    username_verification_steps['Username must not exceed 50 characters'] = bool(re.match(rulle_pattern_02, username))
    
    validation_result = True
    for i in username_verification_steps:
        if username_verification_steps[i] is False:
            validation_result = False
            break

    return (validation_result, username_verification_steps)


def password_validation(password: str) -> tuple:
    """
    Validate the format of a password.

    Parameters:
    password (str): The password to be validated.

    Regular expression pattern:
    ^ - Start of the string.
    (?=.*[0-9]) - Ensuring the presence of at least one digit (0-9).
    (?=.*[A-Z]) - Ensuring the presence of at least one uppercase letter (A-Z).
    .{8,} - Matches any character (except newline) at least 8 or more times.
    $ - End of the string.

    Returns:
    bool: True if the password is valid, False otherwise.
    """
    pass_verification_steps = {"Password must contain at least 8 characters": False,
                              "Password must contain at least one digit": False,
                              "Password must contain at least one uppercase letter": False}

    # Password must contain at least 8 characters
    rulle_pattern_01 = r".{8,}$"
    #Password must contain at least one digit
    rulle_pattern_02 = r".*\d+.*"
    #Password must contain at least one uppercase letter
    rulle_pattern_03 = r".*[A-Z]+.*"

    pass_verification_steps['Password must contain at least 8 characters'] = bool(re.match(rulle_pattern_01, password))
    pass_verification_steps['Password must contain at least one digit'] = bool(re.match(rulle_pattern_02, password))
    pass_verification_steps['Password must contain at least one uppercase letter'] = bool(re.match(rulle_pattern_03, password))

    validation_result = True
    for i in pass_verification_steps:
        if pass_verification_steps[i] is False:
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
    except UsernameValidationError:
        return [x for x in username_validation_result[1] if username_validation_result[1][x] is False]

    try:
        if password_validation_result[0] is False:
            raise PasswordValidationError("Password error validation!")
    except PasswordValidationError:
        return [x for x in password_validation_result[1] if password_validation_result[1][x] is False]

    return (username_validation_result[0], password_validation_result[0])


for name_and_pass in username_and_password_data.items():
    print(f"Name: {name_and_pass[0]}")
    print(f"Password: {name_and_pass[1]}")

    status = list()
    check_name_and_pass = user_validate(name_and_pass[0], name_and_pass[1])

    if check_name_and_pass == (True, True):
        status.append('OK')
        status.append('\n')
    else:
        status.append("ERROR: Validation failed\n")
        for validation_error_text in check_name_and_pass:
            status.append(f"{validation_error_text}")
            status.append('\n')
    status.pop()

    print(f"Status: {''.join(status)}")
    print("-----------------")
