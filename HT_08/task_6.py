"""
Task_6:
Напишіть функцію,яка прймає рядок з декількох слів і повертає довжину
найкоротшого слова. Реалізуйте обчислення за допомогою генератора.
"""


def count_word_in_string(string_check: str) -> int:
    """
    Find and return the length of the shortest word in a given string of multiple words.
    """

    return min(len(x) for x in string_check.split(" "))


print(count_word_in_string("Again you show yourselves you wavering Forms"))
