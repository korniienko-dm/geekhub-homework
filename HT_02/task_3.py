"""
Write a script which accepts a <number> from user and print out a sum of
the first <number> positive integers.
"""


number_user_input = int(input('Please write number:\n'))

sum_positive_int = 0
for i in range(1, (number_user_input + 1)):
    sum_positive_int += i

print(sum_positive_int)