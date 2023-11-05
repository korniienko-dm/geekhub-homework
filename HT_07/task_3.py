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


usernames_and_passwords_data = [['na', 'mypaSS123'],
                               ['username002', 'Password'],
                               ['username003', 'password1'],
                               ['usernmae004', 'Mypass32332'],
                               ['firstname', 'psPS001abc'],
                               ['nameUser01', 'vordPASS022'],
                               ['cc', 'AAgfrfdret'],
                               ['usernmae', 'sOmePassword'],
                               ['usrINsytem', '12ZHGsometext'],
                               ['aa', 'abc'],
                               ['usernmae001', 'abc']]

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
    tuple:
        - tuple[0] containing the validation result for the username;
        - tuple[1] containing the validation result for the password;
        - tuple[2] list of failed validation steps for the username;
        - tuple[3] list of failed validation steps for the password.
    """
    try:
        if not isinstance(username, str):
            raise TypeError("TypeError: 'username' variable must be a <str> only!")

        if not isinstance(password, str):
            raise TypeError("TypeError: 'password' variable must be a <str> only!")

    except TypeError as text_error:
        return text_error
    else:
        username_validation_req = usernmae_validation(username)
        password_validation_req = password_validation(password)

        username_validation_result = username_validation_req[0]
        password_validation_result = password_validation_req[0]

        username_check_step = username_validation_req[1]
        password_check_step = password_validation_req[1]

        username_error_step = [x for x in username_check_step if username_check_step[x] is False]
        password_error_step = [x for x in password_check_step if password_check_step[x] is False]

        return (username_validation_result, password_validation_result, username_error_step, password_error_step)


for user_pass in usernames_and_passwords_data:
    try:
        if not isinstance(user_pass[0], str):
            raise TypeError("TypeError: 'username' variable must be a <str> only!")

        if not isinstance(user_pass[1], str):
            raise TypeError("TypeError: 'password' variable must be a <str> only!")

    except TypeError as text_error:
        print(text_error)
        break
    else:
        print(f"Name: {user_pass[0]}")
        print(f"Password: {user_pass[1]}")

        status = list()
        check_name_and_pass = user_validate(user_pass[0], user_pass[1])

        if check_name_and_pass[0] == (True) and check_name_and_pass[1] == (True):
            status.append('OK')
            status.append('\n')
        else:
            status.append("ERROR: Validation failed\n")
            for validation_error_text in check_name_and_pass[2] + check_name_and_pass[3]:
                status.append(f"{validation_error_text}")
                status.append('\n')
        status.pop()

        print(f"Status: {''.join(status)}")
        print("-----------------")
