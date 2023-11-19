# pylint: disable=missing-function-docstring
"""
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних. Більше ніяких файлів.
      Якщо в попередньому завданні ви добре продумали структуру програми то у
      вас не виникне проблем швидко адаптувати її до нових вимог.
    
    - на старті додати можливість залогінитися або створити новго користувача
      (при створенні новго користувача, перевіряється відповідність логіну і
      паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    
    - в таблиці (базі) з користувачами має бути створений унікальний
      користувач-інкасатор, який матиме розширені можливості (домовимось,
      що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    
    - банкомат має власний баланс
    
    - кількість купюр в банкоматі обмежена. Номіналикупюр - 10, 20, 50, 100, 200, 500, 1000
    
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі
      може лише інкасатор
   
    - користувач через банкомат може покласти на рахунок лише сумму кратну
      мінімальному номіналу що підтримує банкомат. В іншому випадку - повернути
      "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати
      на баланс/кількість купюр банкомату, лише збільшуєтсья баланс користувача
      (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною
      (не вірний логін/пароль, недостатньо коштів на раунку, неможливо видати суму
      наявними купюрами тощо.)
"""


import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DB_NAME = 'best_bank.db'


def update_banknote_counts(denominations: int, new_value: int):
    """
    Update the quantity of a specific banknote denomination in the database.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE banknote_denominations_count
            SET quantity = ?
            WHERE denominations = ?
        """, (new_value, denominations))
    conn.commit()


def get_user_id(username: str):
    """
    Retrieve the user ID associated with the given username from the database.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        return cursor.fetchone()[0]


def get_user_balance(username: str):
    """
    Retrieve the balance associated with the given username from the database.
    """
    user_id = get_user_id(username)
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users_balance WHERE user_id = ?", (user_id,))
        return cursor.fetchone()[0]


def get_total_balance_atm():
    """
    Retrieve the total balance of the ATM, calculated from the quantity of each banknote denomination.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(denominations * quantity)
            FROM banknote_denominations_count
        """)
        total_balance = cursor.fetchone()[0]
        return total_balance


def create_transaction(username: str, operation: str, status: str, transaction_amount: int):
    """
    Create a transaction record in the database, capturing details such as the
    username, type of operation, status, and transaction amount.
    """
    user_id = get_user_id(username)
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO transactions (user_id, operation, status, transaction_amount)
                          VALUES (?, ?, ?, ?)""",
                      (user_id, operation, status, transaction_amount))
    conn.commit()


def initialization_user_balance(username: str):
    """
    Initialize the user balance by creating a record in the database
    with an initial balance of zero for the given username.
    """
    user_id = get_user_id(username)
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users_balance (user_id, balance) VALUES (?, ?)",
                       (user_id, 0))
    conn.commit()


def create_user(username: str, password: str, user_status='user'):
    """
    Create a new user in the database with the specified username,
    password, and optional user status, initializing their balance.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, user_status)VALUES (?, ?, ?)",
                       (username, password, user_status))
    initialization_user_balance(username)
    conn.commit()


def get_user_status(username: str):
    """
    Retrieve the user status (e.g., 'user' or 'inkasator')
    associated with the given username from the database.
    """
    user_id = get_user_id(username)
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_status
            FROM users
            WHERE user_id = ?
        """, (user_id,))
    return cursor.fetchone()[0]


def add_money_to_user_balace(amount: int, username: str):
    """
    Increase the balance of the specified user in the database by the given amount.
    """
    user_id = get_user_id(username)
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users_balance
            SET balance = balance + ?
            WHERE user_id = ?
        """, (amount, user_id))
    conn.commit()


def withdraw_money_from_user_balance(amount: int, username: str):
    """
    Decrease the balance of the specified user in the database
    by the given amount during a money withdrawal.
    """
    user_id = get_user_id(username)
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users_balance
            SET balance = balance - ?
            WHERE user_id = ?
        """, (amount, user_id))
    conn.commit()


def check_user_exists(username: str):
    """
    Check if a user with the specified username exists in the
    database and return True if found, otherwise False.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM users
            WHERE username = ?
        """, (username,))

        return bool(cursor.fetchone())


def get_min_denominations():
    """
    Retrieve the minimum banknote denomination value from the database.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT MIN(denominations)
            FROM banknote_denominations_count
        """)
        return cursor.fetchone()[0]


def check_banknote_denominations_quantity() -> dict:
    """
    Retrieve the quantity of each banknote denomination from the
    database and return the result as a dictionary.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT denominations, quantity
            FROM banknote_denominations_count
        """)
        return dict(cursor.fetchall())


def change_denominations_quantity(banknote_denomination: int, new_quantity: int):
    """
    Change the quantity of a specific banknote denomination in
    the database to the specified new value.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE banknote_denominations_count
            SET quantity = ?
            WHERE denominations = ?
        """, (new_quantity, banknote_denomination))
    conn.commit()


def check_user_password(username: str, password: str):
    """
    Check if the provided username and password match a user
    record in the database, returning True if a match is found, otherwise False.
    """
    with sqlite3.connect(BASE_DIR / DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM users
            WHERE username = ?
            AND
            PASSWORD = ?
        """, (username, password))
        return bool(cursor.fetchone())


def validate_username_conditions(username: str) -> tuple:
    """
    Validate if a username meets specified conditions, checking for minimum
    and maximum length, and ensuring it consists only of Latin letters or numbers.
    """
    username_verification_steps = {"Username must contain at least 3 characters": False,
                                   "Username must not exceed 50 characters": False,
                                   "Username contains only latin letter or number": False}
    rule_pattern_01 = len(username) >= 3
    rule_pattern_02 = len(username) <= 50
    rule_pattern_03 = all((i.isalpha() or i.isnumeric()) and i.isascii() for i in username)
    
    username_verification_steps['Username must contain at least 3 characters'] = rule_pattern_01
    username_verification_steps['Username must not exceed 50 characters'] = rule_pattern_02
    username_verification_steps['Username contains only latin letter or number'] = rule_pattern_03

    validation_result = all(username_verification_steps[step] for step in username_verification_steps)
    
    error_report = list()
    for key in username_verification_steps:
        if username_verification_steps[key] is False:
            error_report.append(key)
    return (validation_result, error_report)


def validate_password_conditions(password: str) -> tuple:
    """
    Validate if a password meets specified conditions, including minimum
    and maximum length, the presence of an uppercase letter, and at least one digit.
    """
    pass_verification_steps = {"Password must contain at least 8 characters": False,
                              "Password must not exceed 50 characters": False,
                              "Password must contain at least one uppercase letter": False,
                              "Password must contain at least one digit": False}

    rule_pattern_01 = len(password) >= 8
    rule_pattern_02 = len(password) <= 50
    rule_pattern_03 = any(char.isupper() for char in password)
    rule_pattern_04 = any(char.isdigit() for char in password)

    pass_verification_steps['Password must contain at least 8 characters'] = rule_pattern_01
    pass_verification_steps['Password must not exceed 50 characters'] = rule_pattern_02
    pass_verification_steps['Password must contain at least one uppercase letter'] = rule_pattern_03
    pass_verification_steps['Password must contain at least one digit'] = rule_pattern_04

    validation_result = all(pass_verification_steps[step] for step in pass_verification_steps)

    error_report = list()
    for key in pass_verification_steps:
        if pass_verification_steps[key] is False:
            error_report.append(key)
    return (validation_result, error_report)


def get_result_user_authentication() -> dict:
    """
    Validate user login and password against a CSV file and return the result as a dictionary
    """
    header_msg = ["\n[-----------------------------]\n",
                    "[           Sign In           ]\n",
                    "[-----------------------------]\n",]
    print("".join(header_msg))

    entered_username = input('Please enter your "Username":\n')
    entered_password = input('\nPlease enter your "Password":\n')
    
    status_check_username = check_user_exists(username=entered_username)
    status_check_password = check_user_password(username=entered_username, password=entered_password)

    verification_result = {'username_status': status_check_username,
                           'password_status': status_check_password,
                           'username': entered_username}
    return verification_result


def put_money_on_balance(username: str) -> str:
    """
    Add money to the balance for the specified username, with the operation
    status indicating success or failure.
    """
    users_current_balance = get_user_balance(username)
    operation = "add money"
    operation_status = "failed"
    min_denomination = get_min_denominations()

    usern_input = input('\nPlease enter the replenishment amount:\n(or "exit" to return previous menu)\n')
    if usern_input == 'exit':
        return "\n[*** Exit. Operation not completed! ***]\n"
    
    try:
        replenishment_amount = int(usern_input)
        if replenishment_amount < 0:
            raise ValueError("The value must be greater than zero!")

    except ValueError as text_error:
        create_transaction(username=username, operation=operation, status=operation_status, transaction_amount=replenishment_amount)
        return f"\n[*** ValueError: {text_error} ***]\n"

    else:
        return process_successful_put_money(replenishment_amount=replenishment_amount, min_denomination=min_denomination, username=username)


def process_successful_put_money(replenishment_amount, min_denomination, username):
    """
    Process a successful money replenishment, updating the user
    balance and creating a transaction record in the database.
    """
    operation_status = "success"
    operation = "add money"
    if replenishment_amount % min_denomination == 0:
        add_money_to_user_balace(amount=replenishment_amount, username=username)
        create_transaction(username=username, operation=operation, status=operation_status, transaction_amount=replenishment_amount)
        return f"\n[ *** Balance successfully increased by {replenishment_amount} USD; ***]"
    else:
        change = replenishment_amount % min_denomination
        replenishment_amount -= change
        add_money_to_user_balace(amount=replenishment_amount, username=username)
        create_transaction(username=username, operation=operation, status=operation_status, transaction_amount=replenishment_amount)
        return f"\n[ *** Balance successfully increased by {replenishment_amount} USD; your change is {change} USD. ***]"


def withdraw_money(username: str) -> str:
    """
    Withdraw money from the balance for the specified username, with the
    operation status indicating success or failure.
    """
    users_current_balance = get_user_balance(username)
    operation = "withdraw money"
    operation_status = "failed"
    min_denomination = get_min_denominations()
    total_balance_atm = get_total_balance_atm()
    user_input = input('\nPlease enter the withdraw amount:\n(or "exit" to return previous menu)\n')
    
    if user_input == 'exit':
        return "\n[*** Exit. Operation not completed! ***]\n"

    try:
        withdraw_amount = int(user_input)
        if withdraw_amount > users_current_balance:
            raise ValueError(
                "There are not enough funds on the balance for this operation!")
        elif (withdraw_amount < users_current_balance) and (withdraw_amount > get_total_balance_atm()):
            raise ValueError(
                "There are not enough funds in the ATM for this operation!")
        
        elif withdraw_amount < 0:
            raise ValueError("The value must be greater than zero!")

    except ValueError as text_error:
        create_transaction(username=username, operation=operation, status=operation_status, transaction_amount=withdraw_amount)
        return f"\n[*** ValueError: {text_error} ***]"

    else:
        return process_successful_withdrawal(withdraw_amount=withdraw_amount, min_denomination=min_denomination, username=username)


def process_successful_withdrawal(withdraw_amount, min_denomination, username):
    """
    Process a successful withdrawal operation, updating the
    user's balance and creating a transaction record.
    """
    operation_status = "success"
    operation = "withdraw money"
    if withdraw_amount % min_denomination == 0:
        withdraw_money_from_user_balance(amount=withdraw_amount, username=username)
        create_transaction(username=username, operation=operation, status=operation_status, transaction_amount=withdraw_amount)
        return "\n[ *** Withdraw has been successfully ***]"
    else:
        change = withdraw_amount % min_denomination
        withdraw_amount -= change
        withdraw_money_from_user_balance(amount=withdraw_amount, username=username)
        create_transaction(username=username, operation=operation, status=operation_status, transaction_amount=withdraw_amount)
        return f"\n[ *** Withdraw {withdraw_amount} USD, has been successfully ***]"


def get_user_menu() -> int:
    """
    Get the user's choice from the main menu, which includes options to
    check balance, add money, withdraw money, and exit.
    """
    run_menu = True
    while run_menu:
        print("\nPlease enter an action: ")
        print("[1] -> Check your balance")
        print("[2] -> Add money")
        print("[3] -> Withdraw money")
        print("[4] -> Exit")
        return input()


def get_first_screen_menu() -> int:
    print("\nPlease enter an action: ")
    print("[1] -> Sign In")
    print("[2] -> Sign Up (if you don't have an account yet.)")
    print("[3] -> Exit")
    return input()


def display_banknote_counts():
    banknote_counts = check_banknote_denominations_quantity()
    print("\n[*** Denominations quantity for the banknotes ***]\n")
    for denomination, count in banknote_counts.items():
        print(f"[ {str(denomination).rjust(4)} ] dollar banknote in quantity of [ {count} ] items.")


def change_denomination_quantity():
    """
    Change the quantity of banknotes in an ATM. Display a menu of
    banknote denominations and prompt the user to enter a number to modify the quantity.
    """
    service_banknot_type = {'1': 10,
                            '2': 20,
                            '3': 50,
                            '4': 100,
                            '5': 200,
                            '6': 500,
                            '7': 1000}

    print("\n[*** Changing the number of banknotes in an ATM ***]")
    print("Please enter the number of the banknote for which you wish to change the quantity:")
    for key, value in service_banknot_type.items():
        print(f"[{key}] -> {value}")

    number_banknote = input("\nEnter a banknote number (or '0' for exit):\n")

    if number_banknote == '0':
        return

    if number_banknote not in service_banknot_type:
        print("\n[*** Error: Invalid banknote number ***]")
        return

    try:
        new_quantity_value = int(input(f"Enter the new value for the quantity of banknotes with a denomination of: {service_banknot_type[number_banknote]} USD: "))
        if new_quantity_value <= 0:
            print("Error: Enter a positive number other than zero")
        else:
            change_denominations_quantity(banknote_denomination=service_banknot_type[number_banknote], new_quantity=new_quantity_value)
            print("\n[*** Value for the quantity of banknotes successfully changed ***]")
    except ValueError as text_error:
        print(f"Error: Enter an integer. {text_error}")


def inkasator_menu():
    """
    Incasator service menu providing options to display banknote
    denominations quantity, change denominations quantity, or exit.
    """
    while True:
        header_msg = ["\n[----------------------------]\n",
                      "[   Incasator Service Menu   ]\n",
                      "[----------------------------]\n",
                      "\nPlease enter an action:\n",
                      "[1] -> Display the denominations quantity for the banknotes\n",
                      "[2] -> Change the denominations quantity\n",
                      "[3] -> Exit\n",]
        print("".join(header_msg))

        incasator_choice = input()

        if incasator_choice == '1':
            display_banknote_counts()
            input("\nPress Enter to continue...")

        elif incasator_choice == '2':
            change_denomination_quantity()
            input("Press Enter to continue...")

        elif incasator_choice == '3':
            return "\n[*** Incasator has successfully logged out ***]\n"


def get_username_for_registration() -> str:
    """
    Prompt the user to create a username for registration, enforcing rules
    such as a minimum of 3 characters, a maximum of 50 characters, and
    consisting only of Latin letters or numbers.
    """
    print("\nPlease create a username:")
    username_rules = [" - Username must contain at least 3 characters;\n",
                      " - Username must not exceed 50 characters;\n",
                      " - Username contains only Latin letter or number.\n"]
    print("".join(username_rules))

    while True:
        username = input('\nEnter your "username":\n')
        if check_user_exists(username):
            print(f'[*** Error: Username "{username}" is already in use! ***]\n')
        else:
            result_check_username = validate_username_conditions(username)
            if result_check_username[0] is False:
                print("\n")
                for error in result_check_username[1]:
                    print(f"[*** Error: {error} ***]")
            else:
                return username


def get_password_for_registration() -> str:
    """
    Prompt the user to create a password for registration, following rules
    such as a minimum of 8 characters, a maximum of 50 characters, containing
    at least one uppercase letter, and at least one digit.
    """
    print("\nPlease create a password:")
    password_rules = [" - Password must contain at least 8 characters;\n",
                      " - Password must not exceed 50 characters;\n",
                      " - Password must contain at least one uppercase letter;\n",
                      " - Password must contain at least one digit.\n"]
    print("".join(password_rules))

    while True:
        password = input('\nEnter your "password":\n')
        result_check_password = validate_password_conditions(password)
        if result_check_password[0] is False:
            print("\n")
            for error in result_check_password[1]:
                print(f"[*** Error: {error} ***]")
        else:
            return password


def registration_new_user() -> str:
    """
    Register a new user by prompting for a valid username and password,
    following specified rules. Returns a success message upon successful registration.
    """
    print("\n[------------------------------]")
    print("[    Registration New User     ]")
    print("[------------------------------]")
    username = get_username_for_registration()
    password = get_password_for_registration()
    create_user(username=username, password=password)
    successfully_msg = [f"\n[*** Congratulations {username}! ***]\n",
                        "You have successfully registered in the system.\n",
                        "Please go to 'home screen' and login, using your username and password."]
    return "".join(successfully_msg)


def hello_screen(username: str) -> str:
    """
    Generate a welcome message for the user with their username on the hello screen.
    """
    return f"\n[*** Hello {username}! Welcome to our ATM! ***]"


def home_screen() -> str:
    """
    Generate a home screen message for the user upon entering the application.
    """
    welcome_banner = ["\n[-----------------------------]\n",
                      "[    Welcome to BEST ATM!     ]\n",
                      "[-----------------------------]"]
    return "".join(welcome_banner)


def start():
    """
    Initialize the application by displaying the home screen, validating
    user credentials, and presenting the main user menu for interactions.
    """
    print(home_screen())

    while True:
        first_menu_selection = get_first_screen_menu()

        if first_menu_selection == '1':
            user_validation = get_result_user_authentication()
            username = user_validation['username']

            if not user_validation['username_status']:
                print("\n[ *** Username is not correct! ***]")
                input("Press Enter to continue...")
            elif not user_validation['password_status']:
                print("\n[ *** Password is not correct! ***]")
                input("Press Enter to continue...")
            else:
                user_status = get_user_status(username)

                if user_status == 'inkasator':
                    print(inkasator_menu())
                elif user_status == 'user':
                    print(hello_screen(username))
                    while True:
                        user_menu_choice = get_user_menu()

                        if user_menu_choice == '1':
                            print(f"\n[ *** Your balance is: {get_user_balance(username)} UDS ***]")
                            input("Press Enter to continue...")
                        elif user_menu_choice == '2':
                            print(put_money_on_balance(username=username))
                            input("Press Enter to continue...")
                        elif user_menu_choice == '3':
                            print(withdraw_money(username=username))
                            input("Press Enter to continue...")
                        elif user_menu_choice == '4':
                            break
        elif first_menu_selection == '2':
            print(registration_new_user())
            input("Press Enter to continue...")
        elif first_menu_selection == '3':
            return f"\nGoodbye, {username}! Thank you for using our bank!\n"


if __name__ == "__main__":
    print(start())
