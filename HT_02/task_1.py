"""
Write a script which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
"""


user_input = input(
    'Please enter sequence of comma-separated numbers \n(example: "1,2,3,4,5"):\n')

list_generate = user_input.split(',')
tuple_generate = tuple(user_input.split(','))

print(f"{list_generate} {type(list_generate)}\n{tuple_generate} {type(tuple_generate)}")