"""
Task_2:
Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна
повертати якийсь результат (напр. інпут від юзера, результат математичної
операції тощо).
Також створiть четверту ф-цiю, яка всередині викликає 3 попереднi,
обробляє їх результат та також повертає результат своєї роботи. Таким
чином ми будемо викликати одну (четверту) функцiю, а вона в своєму
тiлi - ще 3.
"""


hello_string = "\
*************************************\n\
Welcome to simple symbol replacement \n\
*************************************\n"


def get_string_from_usr():
     """
    Function prompts the user to enter a string and returns the input string.
    Returns: str: The string entered by the user.
     """

     usr_string = input("Please enter your string: ")
     return usr_string


def get_wich_symbol_by_replaced():
    """
    Function prompts the user to enter a symbol to be replaced and returns the input symbol.
    Returns: str: The symbol entered by the user for replacement.
    """ 

    usr_char_replaced = input("Enter a symbol that has to be replaced: ")
    return usr_char_replaced


def get_new_symbol_to_replace():
     """
    Function prompts the user to enter a symbol with which another symbol has to be replaced.
    Returns: str: The symbol entered by the user for replacement.
     """

     usr_char_replase = input("Enter a symbol with which it has to be replaced: ")
     return usr_char_replase


def get_string_after_replace():
     """
     Function takes a user string, replaces a specified symbol with another, and returns the modified string.

     Args:
        usr_string (str): The original input string.
        replaced_symbol (str): The symbol to be replaced.
        new_replace_symbol (str): The symbol with which to replace the old symbol.

     Returns: str: The modified string after replacing the specified symbol.     
     """

     user_str = get_string_from_usr()
     symbol_by_replaced = get_wich_symbol_by_replaced()
     new_symbol_to_replace = get_new_symbol_to_replace()

     str_after_replacement = user_str.replace(symbol_by_replaced, new_symbol_to_replace)

     return f'\nYour string after replacing the symbol "{symbol_by_replaced}" with "{new_symbol_to_replace}":\n{str_after_replacement}'


print(hello_string)
print(get_string_after_replace())
