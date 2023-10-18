"""
Write a script which accepts decimal number from user and converts it to hexadecimal.
"""


number_from_usr = int(input(
    '\nPlease enter a "decimal number" to get convert to "hexadecimal number" system:\n'))
convert_to_hexadecimal = hex(number_from_usr)

print(convert_to_hexadecimal)