"""
Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями.
Створiть просту умовну конструкцiю (звiсно вона повинна бути в тiлi ф-цiї),
пiд час виконання якої буде перевiрятися рiвнiсть змiнних "x" та "y" та
у випадку нервіності - виводити ще і різницю.

    Повиннi опрацювати такi умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      вiдповiдь - "х дорiвнює z"
"""


def get_value_difference(x: int, y: int):
    """
    Function checks the equality of two variables, 'x' and 'y', and,
    if they are not equal, calculates and 
    returns the absolute difference between them.

    Parameters:
    - x (int): The first integer to be compared.
    - y (int): The second integer to be compared.   
    """

    x = int(input("Please enter 'X' number:\n"))
    y = int(input("Please enter 'Y' number:\n"))   
    z = abs(x - y)

    if x > y: return (f"'X' biiger than 'Y' by: {z}")
    elif y > x: return (f"'Y' biiger than 'X' by: {z}")
    elif x == y: return (f"'X' equals 'Y'")


print(get_value_difference(x, y))