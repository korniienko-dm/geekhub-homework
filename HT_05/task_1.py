"""
Task_1:
Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12)
та яка буде повертати пору року, якiй цей мiсяць належить (зима, весна, лiто
або осiнь). У випадку некоректного введеного значення - виводити відповідне
повідомлення.
"""


def season(month_number: int):
    """
    This function returns the season of the year based on the provided month number.

    Parameters:
    - month_number (int): The month number (1 to 12) to determine the season for.
    """

    season_of_year = {"winter": [12, 1, 2],
                      "spring": [3, 4, 5],
                      "summer": [6, 7, 8],
                      "autumn": [9, 10, 11]}

    for i in season_of_year:
        if month_number in season_of_year[i]:
            return f"Month number {month_number} - is a {i} month."
            
    return f'Error: Value "{month_number}" is not a correct month number.'


get_user_month = int(input("Please enter number of month: "))
print(season(get_user_month))
