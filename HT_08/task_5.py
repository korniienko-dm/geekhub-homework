"""
Task_5:
Напишіть функцію,яка приймає на вхід рядок та повертає кількість окремих
регістро-незалежних букв та цифр, які зустрічаються в рядку більше ніж
1 раз. Рядок буде складатися лише з цифр та букв (великих і малих).
Реалізуйте обчислення за допомогою генератора.
    Example (input string -> result):
    "abcde" -> 0            # немає символів, що повторюються
    "aabbcde" -> 2          # 'a' та 'b'
    "aabBcde" -> 2          # 'a' присутнє двічі і 'b' двічі (`b` та `B`)
    "indivisibility" -> 1   # 'i' присутнє 6 разів
    "Indivisibilities" -> 2 # 'i' присутнє 7 разів та 's' двічі
    "aA11" -> 2             # 'a' і '1'
    "ABBA" -> 2             # 'A' і 'B' кожна двічі
"""


def count_repeated_alphanumeric_characters(check_string: str) -> str:
    """
    Count the number of unique case-insensitive alphanumeric characters
    that appear more than once in the given string.
    """

    def generator_count(check_string: str) -> int:
        """ Generator """
        lower_check_string = check_string.lower()
        set_check_string = set(lower_check_string)

        for simbol in set_check_string:
            if lower_check_string.count(simbol) > 1:
                yield 1

    return sum(generator_count(check_string))


print(count_repeated_alphanumeric_characters('aA11'))
