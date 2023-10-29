"""
Task_4:
Наприклад маємо рядок --> 
"f98neroi4nr0c3n30irn03ien3c0rfe  kdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p4 65jnpoj35po6j345"
 -> просто потицяв по клавi =)
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього та яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 (включно) -> прiнтує довжину рядка, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр лише з буквами (без пробілів)
-  якщо довжина більше 50 -> щось вигадайте самі, проявіть фантазію =)
"""
import re


def string_calc_simbol(row_checked: str):
    """
    Function checks the contents of the row and processes different
    scenarios based on the number of characters.

    Parameters:
    - row_checked (str): The input string to be checked.
    """

    symbol_len = len(row_checked)
    char_count = [x for x in row_checked if x.isalpha()]
    number_count = [int(x) for x in row_checked if x.isdigit()]

    digits_patern = r'[0-9]+'
    digits_count = re.findall(digits_patern, row_checked)
    digits_count = list(map(int, digits_count))
    digits_count = [i for i in digits_count if i != 0]


    if (30 <= len(row_checked) <= 50):
        output_row_count = f"\nRow length: {symbol_len}\n"      
        output_letter_count = f"Count of letters in a row: {len(char_count)}\n"
        output_number_count = f"Count of numbers in a row: {len(number_count)}"
        return f"{output_row_count}{output_letter_count}{output_number_count}"

    elif (len(row_checked) < 30):
        sum_all_digit = f"\nSum all digits in row: {sum(digits_count)}\n"
        all_char_symbol = f"All char symbol: {''.join(char_count)}"
        return (f'{sum_all_digit}{all_char_symbol}')
    
    elif (len(row_checked) > 50):
        hash_from_row = hash(row_checked)
        return f"\nThe result of a hash function for a row: \n{hash_from_row}"
        

user_input = input("Please enter your string:\n")        

print(string_calc_simbol(user_input))
