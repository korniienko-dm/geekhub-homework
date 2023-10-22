"""
Taks_9:
Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе
всі високосні роки в цьому проміжку (границі включно). P.S. Рік є високосним,
якщо він кратний 4, але не кратний 100, а також якщо він кратний 400.
"""


print("\n*** CHECK 'LEAP YEARS' IN A RANGE OF YEARS  ***")

user_input_start_year = int(input("\nEnter the starting year in the range:\n"))
user_input_end_year = int(input("\nEnter the ending year in the range\n"))

for year in range(user_input_start_year, (user_input_end_year + 1)):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year)
    else:
        continue
