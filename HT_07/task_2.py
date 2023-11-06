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


class LoginException(Exception):
    """Custom exception class for login errors."""


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
    Validate the format of a password..
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
    username_validation_result = usernmae_validation(username)
    password_validation_result = password_validation(password)

    try:
        if username_validation_result[0] is False:
            raise LoginException("\n".join([x for x in username_validation_result[1] if username_validation_result[1][x] is False]))

        if password_validation_result[0] is False:
            raise LoginException("\n".join([x for x in password_validation_result[1] if password_validation_result[1][x] is False]))

    except LoginException as text_error:
        return f"LoginException:\n{text_error}"
    else:
        return (username_validation_result[0], password_validation_result[0])


print(user_validate(username="uss", password="some"))
