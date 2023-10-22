"""
Taks_7:
Write a script which accepts a <number> from user and generates dictionary
in range <number> where key is <number> and value is <number>*<number>
    e.g. 3 --> {0: 0, 1: 1, 2: 4, 3: 9}
"""


user_input = input("Please enter a number: \n")
my_dict = dict()

for i in range(int(user_input)+1):
    my_dict[i] = i * i

print(my_dict)
