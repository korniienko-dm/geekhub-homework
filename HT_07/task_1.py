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
    db_users = {
        'user_001': 'somepass001',
        'user_002': 'somepass002',
        'user_003': 'somepass003',
        'user_004': 'somepass004',
        'user_005': 'somepass005'}

    return db_users


def check_user_verification(username: str, password: str, database: dict) -> bool:
    """
    Verify user credentials against the given database.

    Parameters:
    username (str): The username to verify.
    password (str): The password to verify.
    database (dict): The user database to check against.

    Returns:
    bool: True if the provided credentials match the database, False otherwise.
    """
    result = database.get(username) == password

    return result


def get_autentification_result(username: str, password: str, silent=False):
    """
    Authenticate a user and return the authentication result.

    Parameters:
    username (str): The username to authenticate.
    password (str): The password to use for authentication.
    silent (bool, optional): If True, suppress exceptions and return a
    boolean result. If False, raise an exception in case of authentication
    failure.

    Returns:
    bool or str: If "silent" is True, return a boolean indicating the
    authentication result. If silent is False, return an exception
    message in case of authentication failure.
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
