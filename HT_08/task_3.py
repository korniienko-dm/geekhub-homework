"""
Task_3:
Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по
   ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (аналог range(1, -10, 5)).
   Подивіться як веде себе стандартний range в таких випадках.
"""


def my_range(*args):
    """
    Return an object that produces a sequence of integers from start (inclusive)
    to stop (exclusive) by step.
    """
    start = 0
    stop = 0
    step = 1

    if len(args) > 3:
        raise TypeError("my_range expected at most 3 arguments")
    if len(args) == 0:
        raise TypeError("my_range expected at least 1 argument, got 0")
    for argumnet in args:
        if not isinstance(argumnet, int):
            raise TypeError("invalid argument type - my_range accept only <int>")
    
    if len(args) == 1:
        stop = args[0]
    if len(args) == 2:
        start, stop = args[0], args[1]
    if len(args) == 3:
        start, stop, step = args[0], args[1], args[2]

    count_value = start

    while (step > 0 and count_value < stop) or (step < 0 and count_value > stop):
        yield count_value
        count_value += step


print(list(my_range(1, 55, 2)))
