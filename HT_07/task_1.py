"""
Task_1:
Створіть функцію, всередині якої будуть записано список із п'яти користувачів
(ім'я та пароль). Функція повинна приймати три аргументи: два - обов'язкових
(<username> та <password>) і третій - необов'язковий параметр <silent>
(значення за замовчуванням - <False>).
Логіка наступна:
    якщо введено коректну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція вертає False
        якщо silent == False -породжується виключення LoginException (його
        також треба створити =))
"""


class LoginException(Exception):
    """Custom exception class for login errors."""


def get_data_base() -> dict:
    """Return a database of user credentials as a dictionary."""
    db_users = [{'username': 'user_001', 'password': 'somepass001'},
                {'username': 'user_002', 'password': 'somepass002'},
                {'username': 'user_003', 'password': 'somepass003'},
                {'username': 'user_004', 'password': 'somepass004'},
                {'username': 'user_005', 'password': 'somepass005'},]
    return db_users


def check_user_verification(username: str, password: str, database: dict) -> bool:
    """
    Verify user credentials against the given list of dictionaries.
    """
    for user in database:
        if user['username'] == username and user['password'] == password:
            return True
    return False


def get_autentification_result(username: str, password: str, silent=False):
    """
    Validate user credentials and return the result.

    If "silent mode" is True and authentication fails, the function will return
    False instead of raising exceptions.

    If "silent mode" is False (default), and authentication fails, a LoginException
    will be raised with an error message.
    """

    result_check = check_user_verification(username, password, database=get_data_base())

    if bool(not result_check and silent):
        result_check = False
    elif bool(not result_check and not silent):
        try:
            raise LoginException("Login Exception error.")
        except LoginException as text_error:
            return f"Error, detail: {text_error}"

    return result_check


print(get_autentification_result(username='user_001', password='somepass001'))
