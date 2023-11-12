"""
Task_1:
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після запуска
   програми на екран виводиться в лівій половині - колір автомобільного,
   а в правій - пішохідного світлофора. Кожну 1 секунду виводиться поточні
   кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка
   така сама як і в звичайних світлофорах (пішоходам зелений тільки коли
   автомобілям червоний).

   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""
import time


def get_traffic_work_list():
    """
    Get a list representing the changing states of a traffic light for cars and pedestrians.
    """
    traffic_light_mode = [{'cars': 'Red', 'pedestrians': 'Green'},
                          {'cars': 'Red', 'pedestrians': 'Green'},
                          {'cars': 'Red', 'pedestrians': 'Green'},
                          {'cars': 'Red', 'pedestrians': 'Green'},
                          {'cars': 'Yellow', 'pedestrians': 'Red'},
                          {'cars': 'Yellow', 'pedestrians': 'Red'},
                          {'cars': 'Green', 'pedestrians': 'Red'},
                          {'cars': 'Green', 'pedestrians': 'Red'},
                          {'cars': 'Green', 'pedestrians': 'Red'},
                          {'cars': 'Green', 'pedestrians': 'Red'},
                          {'cars': 'Yellow', 'pedestrians': 'Red'},
                          {'cars': 'Yellow', 'pedestrians': 'Red'},]
    return traffic_light_mode


def run_traffic_light(itration_object):
    """
    Simulate the operation of a traffic light using an iterable,
    providing states in a loop with a one-second interval
    """
    while True:
        for item in itration_object:
            time.sleep(1)
            yield item


traffic_light = run_traffic_light(get_traffic_work_list())

print("Simple Traffic Light:")
print('🚙'.center(6), end=" ")
print('🙎'.center(6))

for i in traffic_light:
    print(i['cars'].center(6), end="  ")
    print(i['pedestrians'].center(6))
