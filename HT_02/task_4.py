"""
Write a script which accepts a <number> from user and then <number> times
asks user for string input. At the end script must print out result of
concatenating all <number> strings.
"""


num_count_string_input = int(input("Please enter a number:\n"))
list_concatenating = list()

for i in range(1, num_count_string_input + 1):
    inp_optional_str = input(
        f"\nEnter {i} optional string of {num_count_string_input} expected strings:\n")
    list_concatenating.append(inp_optional_str)

str_result_concatenating = "".join(list_concatenating)
print(str_result_concatenating)