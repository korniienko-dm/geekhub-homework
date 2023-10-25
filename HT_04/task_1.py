"""
Task_1:
Написати скрипт, який приймає від користувача два числа (int або float) і
робить наступне: Кожне введене значення спочатку пробує перевести в int.
У разі помилки - пробує перевести в float, а якщо і там ловить
помилку - пропонує ввести значення ще раз (зручніше на даному етапі
навчання для цього використати цикл while) Виводить результат ділення
першого на друге. Якщо при цьому виникає помилка - оброблює її і виводить
відповідне повідомлення.
"""


while True:

    value_1 = input("Please enter a first number: ")
    value_2 = input("Please enter a second number: ")

    try:
        value_1 = int(value_1)
        value_2 = int(value_2)

    except Exception as unknown_error:
        print(f"\nError: {unknown_error}.\nScript try convert it to float...")

        try:
            value_1 = float(value_1)
            value_2 = float(value_2)

        except Exception as unknown_error:
            print(f"\nError: {unknown_error}.\nPlease enter your value again:\n")
            continue

    try:
        print(
            f"Result of the division {value_1} on {value_2}: {value_1 / value_2} ")
        break

    except Exception as unknown_error:
        print(f"Error: {unknown_error}")
        break
