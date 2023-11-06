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


def get_data_base_users() -> list:
    """Return a list of user credentials (username, password) as dictionaries."""
    db_users = [{'username': 'na', 'password': 'mypaSS123'},
                {'username': 'username002', 'password': 'Password'},
                {'username': 'username003', 'password': 'password1'},
                {'username': 'usernmae004', 'password': 'Mypass32332'},
                {'username': 'firstname', 'password': 'psPS001abc'},
                {'username': 'nameUser01', 'password': 'vordPASS022'},
                {'username': 'cc', 'password': 'AAgfrfdret'},
                {'username': 'usernmae', 'password': 'sOmePassword'},
                {'username': 'usrINsytem', 'password': '12ZHGsometext'},
                {'username': 'aa', 'password': 'abc'},
                {'username': 'usernmae001', 'password': 'abc'},]
    return db_users


def usernmae_validation(username: str) -> tuple:
    """
    Validate the format of a username.
    """
    username_verification_steps = {"Username must contain at least 3 characters": False,
                                   "Username must not exceed 50 characters": False,}

    rulle_pattern_01 = len(username) >= 3
    rulle_pattern_02 = len(username) <= 50
    
    username_verification_steps['Username must contain at least 3 characters'] = bool(rulle_pattern_01)
    username_verification_steps['Username must not exceed 50 characters'] = bool(rulle_pattern_02)
    
    validation_result = True
    for step in username_verification_steps:
        if username_verification_steps[step] is False:
            validation_result = False
            break

    return (validation_result, username_verification_steps)


def password_validation(password: str) -> tuple:
    """
    Validate the format of a password.
    """
    pass_verification_steps = {"Password must contain at least 8 characters": False,
                              "Password must contain at least one digit": False,
                              "Password must contain at least one uppercase letter": False}

    rulle_pattern_01 = len(password) >= 8
    rulle_pattern_02 = any(char.isdigit() for char in password)
    rulle_pattern_03 = any(char.isupper() for char in password)

    pass_verification_steps['Password must contain at least 8 characters'] = bool(rulle_pattern_01)
    pass_verification_steps['Password must contain at least one digit'] = bool(rulle_pattern_02)
    pass_verification_steps['Password must contain at least one uppercase letter'] = bool(rulle_pattern_03)

    validation_result = True
    for step in pass_verification_steps:
        if pass_verification_steps[step] is False:
            validation_result = False
            break

    return (validation_result, pass_verification_steps)


def user_validate(username: str, password: str) -> tuple:
    """
    Validate a username and password.
    """
    username_validation_req = usernmae_validation(username)
    password_validation_req = password_validation(password)

    username_validation_result = username_validation_req[0]
    password_validation_result = password_validation_req[0]

    username_check_step = username_validation_req[1]
    password_check_step = password_validation_req[1]

    username_error_step = [x for x in username_check_step if username_check_step[x] is False]
    password_error_step = [x for x in password_check_step if password_check_step[x] is False]

    return (username_validation_result, password_validation_result, username_error_step, password_error_step)


for data_base_users in get_data_base_users():
    try:
        if not isinstance(data_base_users['username'], str):
            raise TypeError("TypeError: 'username' variable must be a <str> only!")

        if not isinstance(data_base_users['password'], str):
            raise TypeError("TypeError: 'password' variable must be a <str> only!")

    except TypeError as text_error:
        print(text_error)
        break
    
    else:
        print(f"Name: {data_base_users['username']}")
        print(f"Password: {data_base_users['password']}")

        status = list()
        check_name_and_pass = user_validate(data_base_users['username'], data_base_users['password'])

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
