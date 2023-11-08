"""
Task_7:
Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список, в
якому знаходяться елементи першого списку, яких немає в другому. Порядок
елементів, що залишилися має відповідати порядку в першому (оригінальному)
списку. Реалізуйте обчислення за допомогою генератора.
    Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 4, 3, 4], [2]) --> [1, 4, 3, 4]
"""


def get_different_array(first_list: list, second_list: list) ->  list:
    """
    Return a list containing elements from the first_list that are not found in the second_list.
    """

    return list((ellement for ellement in first_list if not second_list.count(ellement)))


print(get_different_array([1, 2, 2, 2, 4, 3, 4], [2]))
