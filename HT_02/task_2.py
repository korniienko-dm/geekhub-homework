"""
Write a script which accepts two sequences of comma-separated colors from 
user. Then print out a set containing all the colors from color_list_1
which are not present in color_list_2.
"""


usr_input_color_list_1 = input(
    '\nPlease enter the "first list" of colors:\n(values separated by commas, for example: "black,white,blue")\n')
color_list_1 = usr_input_color_list_1.split(',')

usr_input_color_list_2 = input(
    '\nPlease enter the "second list" of colors:\n(values separated by commas, for example: "black,white,blue")\n')
color_list_2 = usr_input_color_list_2.split(',')

set_color_difference = set(color_list_1).difference(set(color_list_2))

print(set_color_difference)