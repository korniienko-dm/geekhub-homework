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

    for season_name, season_month_number in season_of_year.items():
        if month_number in season_month_number:
            return f"Month number {month_number} - is a {season_name} month."
            
    return f'Error: Value "{month_number}" is not a correct month number.'


try:
    get_user_month = int(input("Please enter number of month: "))

except ValueError as text_error:
    print(f"Error!: Details: {text_error}")

else:
    print(season(get_user_month))
