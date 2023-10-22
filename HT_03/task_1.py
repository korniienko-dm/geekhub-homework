"""
Task_1:
Write a script that will run through a list of tuples and replace the 
last value for each tuple. The list of tuples can be hardcoded. The
"replacement" value is entered by user. The number of elements in the
tuples must be different.
"""


list_of_tuple = [(1, 2, 3, 4, 5),
                 ('a', 'b', 'c', 'd', 'e'),
                 ('Berlin', 'Budapest', 'Luxembourg', 'Stockholm'),
                 (True, False),
                 (1,),
                 ('a',)]

print("\n*** REPLACE THE LAST VALUE FOR EACH TUPLE  ***")
print(f"\nOur list of tuples:\n{list_of_tuple}\n")

user_input_value = input(
    'Please input your value for replace the last value for each tuple:\n')

for i in range(len(list_of_tuple)):
    list_of_tuple[i] = tuple(list_of_tuple[i][:-1] + (user_input_value,))

print(f"\nOur tuple list values after replace:\n {list_of_tuple}")
