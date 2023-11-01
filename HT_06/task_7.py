"""
Task_7:
Написати функцію, яка приймає на вхід список (через кому), підраховує
кількість однакових елементів у ньомy і виводить результат. Елементами
списку можуть бути дані будь-яких типів.
    
Наприклад:
1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
"""


def get_elem_and_he_quantity(check_list:list) -> dict:
    """
    Counts the quantity of each element in the input list.

    Parameters:
    check_list (list): The list to count elements in.

    Returns:
    dict: A dictionary where keys are elements from the input list, and values
          are the counts of how many times each element appears in the list.
    """    
    count_ellem = dict()
    
    for ellement in check_list:
        key = str(ellement)
        
        if key in count_ellem:
            count_ellem[key] += 1
        else:
            count_ellem[key] = 1 
    
    return count_ellem


def get_string_result_count_ellem(count_ellem:dict) -> str:
    """
    Formats the count of elements as a string.

    Parameters:
    count_ellem (dict): A dictionary with element counts.

    Returns:
    str: A string containing element counts in the format "element -> count".
    """    
    list_result = list()
    
    for key, value in count_ellem.items():
        list_result.append(f"{key} -> {value}")
    
    return ", ".join(list_result)


def get_counting_elements(*args) -> str:
    """
    Creates a list from user-provided arguments, counts the elements, and returns
    the result as a formatted string.

    Parameters:
    *args: Variable-length arguments provided by the user.

    Returns:
    str: A string containing element counts in the format "element -> count".
    """    
    check_list = list()
    dict_value = dict()
    list_result = str()
    
    for ellem in args:
        check_list.append(ellem)

    dict_value = get_elem_and_he_quantity(check_list)
    list_result = get_string_result_count_ellem(dict_value)

    return list_result


print(get_counting_elements(1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2]))
