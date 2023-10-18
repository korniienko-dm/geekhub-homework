"""
Write a script to check whether a value from user input is contained in a group of values.

e.g. [1, 2, 'u', 'a', 4, True] --> 2 --> True
     [1, 2, 'u', 'a', 4, True] --> 5 --> False
"""


group_values = [1, 2, 'u', 'a', 4, True]

user_enter_value = input("Please enter value:\n")

result_convert_values_to_str = " ".join(map(str, group_values))

print(user_enter_value in result_convert_values_to_str)