"""
Task_4:
Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність
(рядок, список, кортеж) і повертає генератор, який буде вертати значення з
цієї послідовності, при цьому, якщо було повернено останній елемент із
послідовності - ітерація починається знову.
   
Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in generator([1, 2, 3]):
       print(elem)
   1
   2
   3
   1
   2
   3
   1
   .......
"""


def infinity_generator(itration_object):
    "Simply infinity generator"

    while True:
        for i in itration_object:
            yield i


for element in infinity_generator([1, 2, 3, 4, 5]):
    print(element)
