"""
Write a script to concatenate all elements in a list into a string and print
it. List must be include both strings and integers and must be hardcoded.
"""


item_list = ['a', 'b', 'c', 1, 2, 3, True, False]
convert_list_to_str = " ".join(map(str, item_list))

print(convert_list_to_str)