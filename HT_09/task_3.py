"""
Task_3:
Програма-банкомат.
   Використувуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль
        (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>)
        та історію транзакцій (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених
        даних (введено цифри; знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал
        додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони
        неправильні - вивести повідомлення про це і закінчити роботу.
        (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання
      має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
"""

import csv
import json
from datetime import datetime


WORKING_DIRECTORY = "task_3_file/"


def get_result_user_validation() -> dict:
    """
    Validate user login and password against a CSV file and return the result as a dictionary
    """
    entered_login = input('Please enter your "Login":\n')
    entered_password = input('\nPlease enter your "Password":\n')
    status_check_login = False
    status_check_password = False
    status_check_username = False

    file_path = WORKING_DIRECTORY + "users.csv"
    with open(file_path) as f:
        reader = iter(csv.DictReader(f, delimiter=';'))
        for row in reader:
            if row['login'] == entered_login:
                status_check_login = True
                status_check_username = row['username']
            if row['password'] == entered_password:
              status_check_password = True
        
    verification_result = {'login': status_check_login,
                           'password': status_check_password,
                           'username': status_check_username}
    
    return verification_result


def get_file_path(username: str, working_directory:str, file_postfix: str) -> str:
    """
    Generate and return the file path based on the provided username,
    working directory, and file postfix.
    """
    format_user = username.replace(" ", "_").lower()
    user_file_path = working_directory + format_user + file_postfix
    return user_file_path


def get_balance_value(username: str) -> int:
    """ 
    Retrieve and return the balance value for the specified username, with
    the operation status indicating success or failure.
    """
    user_balance_file = get_file_path(username, WORKING_DIRECTORY, "_balance.txt")
    operation = "balance check"
    operation_status = "failed"

    with open(user_balance_file, 'r', encoding='utf-8') as file:
        get_balace = file.read().replace('\n', '')
        try:
            int(get_balace)
        except ValueError as text_error:
            return text_error
        else:
            operation_status = "Success"
            return int(get_balace)


def put_money_on_balance(username: str) -> str:
    """
    Add money to the balance for the specified username, with the operation
    status indicating success or failure.
    """
    user_balance_file = get_file_path(username, WORKING_DIRECTORY, "_balance.txt")
    users_current_balance = get_balance_value(username)
    operation = "add money"
    operation_status = "failed"

    replenishment_amount = input('Please enter the replenishment amount:\n(or "exit" to return previous menu)\n')
    if replenishment_amount == 'exit':
        return "\n[*** Exit. Operation not completed! ***]\n"
    try:
        if int(replenishment_amount) < 0:
            raise ValueError("The value must be greater than zero!")

    except ValueError as text_error:
        save_transaction(username, operation, operation_status, replenishment_amount, str(users_current_balance))
        return f"\n[*** ValueError: {text_error} ***]\n"

    else:
        with open(user_balance_file, 'w', encoding='utf-8') as file:
            file.write(str(users_current_balance + int(replenishment_amount)))
            operation_status = "success"
            save_transaction(username, operation, operation_status, replenishment_amount, str(users_current_balance))
            return "\n[ *** Balance has been successfully update ***]\n"


def withdraw_money(username: str) -> str:
    """
    Withdraw money from the balance for the specified username, with the
    operation status indicating success or failure.
    """
    user_balance_file = get_file_path(username, WORKING_DIRECTORY, '_balance.txt')
    users_current_balance = get_balance_value(username)
    operation = "withdraw money"
    operation_status = "failed"
    withdraw_amount = input('Please enter the withdraw amount:\n(or "exit" to return previous menu)\n')

    if withdraw_amount == 'exit':
        return "\n[*** Exit. Operation not completed! ***]\n"

    try:
        if int(withdraw_amount) > users_current_balance:
            raise ValueError("There are not enough funds on the balance for this operation!")
        elif int(withdraw_amount) < 0:
            raise ValueError("The value must be greater than zero!")

    except ValueError as text_error:
        save_transaction(username, operation, operation_status, withdraw_amount, str(users_current_balance))
        return f"\n[*** ValueError: {text_error} ***]\n"

    else:
        with open(user_balance_file, 'w', encoding='utf-8') as file:
            file.write(str(users_current_balance - int(withdraw_amount)))
            operation_status = "success"
            save_transaction(username, operation, operation_status, withdraw_amount, str(users_current_balance))
            return "\n[ *** Balance has been successfully update ***]\n"


def save_transaction(username: str, operation_type: str, operation_status: str, tr_amount: str, balance: str):
    """
    Save a transaction record with details such as username, operation type,
    status, transaction amount, and balance before the transaction to a JSON file.
    """
    transaction_id = datetime.now().strftime("%Y%m%d%H%M%S")
    user_transaction_file = get_file_path(username, WORKING_DIRECTORY, "_transactions.json")

    transaction = {"transaction_id": transaction_id,
                   "username": username,
                   "operation": operation_type,
                   "status": operation_status,
                   "transaction_amount": tr_amount,
                   "balance_before_transaction": balance}

    with open(user_transaction_file, 'a', encoding='utf-8') as file:
        json.dump(transaction, file, sort_keys=True, indent=2)
        file.write('\n')


def get_main_user_menu() -> int:
    """
    Get the user's choice from the main menu, which includes options to
    check balance, add money, withdraw money, and exit.
    """
    try:
        print("Please enter an action: ")
        print("[1] -> Check your balance")
        print("[2] -> Add money")
        print("[3] -> Withdraw money")
        print("[4] -> Exit")
        user_choice = int(input())
    except ValueError as text:
        return f"ValueError: {text}"
    else:

        return user_choice


def hello_screen(username: str) -> str:
    """
    Generate a welcome message for the user with their username on the hello screen.
    """
    return f"\n[*** Hello {username}! Welcome to our ATM! ***]\n"


def home_screen() -> str:
    """
    Generate a home screen message for the user upon entering the application.
    """
    first_line = "\n*********************\n"
    second_line = "Welcome to BEST BANK!\n"
    third_line = "*********************"
    return first_line + second_line + third_line


def start():
    """
    Initialize the application by displaying the home screen, validating
    user credentials, and presenting the main user menu for interactions.
    """
    print(home_screen())
    user_validation = get_result_user_validation()

    if user_validation['login'] is False:
        return "\nLogin is not correct!"
    if user_validation['password'] is False:
        return "\nPassword is not correct!"
    
    print(hello_screen(username=user_validation['username']))

    while True:
        user_menu_selection = get_main_user_menu()

        if user_menu_selection == 1:
            print(f"\n[ *** Your balance is: {get_balance_value(username=user_validation['username'])} UDS ***]\n")
        if user_menu_selection == 2:
            print(put_money_on_balance(username=user_validation['username']))
        if user_menu_selection == 3:
            print(withdraw_money(username=user_validation['username']))
        if user_menu_selection == 4:
            return f"\nGoodbuy {user_validation['username']}! Thank you for using our bank!\n"


print(start())
