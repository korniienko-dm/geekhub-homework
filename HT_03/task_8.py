"""
Taks_8:
Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову,
яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.
"""


user_input = int(input("Please enter a number: \n"))

for i in range(user_input + 1):
    if (i % 17) != 0:
        continue
    else:
        print(i)
