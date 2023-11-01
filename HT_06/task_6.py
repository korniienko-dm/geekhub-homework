"""
Task_6:
Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в
списку. Тобто функція приймає два аргументи: список і величину зсуву
(якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна -
навпаки - пересуваємо елементи з початку списку в його кінець).

Наприклад:
fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""


def positive_shift(list_ellem:list) -> list:
    """
    Performs a positive shift of the elements in the input list.

    Parameters:
    list_ellem (list): The list to be shifted.

    Returns:
    list: The input list with elements shifted one position to the right.
    """    
    list_ellem = list_ellem[-1:] + list_ellem[:-1]
    return list_ellem


def negative_shift(list_ellem:list) -> list:
    """
    Performs a negative shift of the elements in the input list.

    Parameters:
    list_ellem (list): The list to be shifted.

    Returns:
    list: The input list with elements shifted one position to the left.
    """    
    list_ellem = list_ellem[1:] + list_ellem[:1]
    return list_ellem


def get_shift_list_elem(user_list, shift) -> list:
    """
    Shifts the elements in the input list by a specified number of positions.

    Parameters:
    user_list (list): The list to be shifted.
    shift (int): The number of positions to shift the elements. A positive
                 value represents a right shift, and a negative value represents
                 a left shift.

    Returns:
    list: The input list with elements shifted by the specified number of positions.
    """    
    if shift >= 0:
        work_function = positive_shift
    else:
        work_function = negative_shift
        shift *= -1

    for i in range(shift):
        user_list = work_function(user_list)
    
    return user_list


print(get_shift_list_elem(user_list=[1, 2, 3, 4, 5], shift=-2))


