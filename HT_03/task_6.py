"""
Taks_6:
Write a script to get the maximum and minimum value in a dictionary.
"""


dict_duplicate = {1: 'Ukraine',
                  2: 'Mexico',
                  3: 'Japan',
                  4: 'Philippines',
                  5: 'Egypt',
                  6: 'Vietnam',
                  7: 'Germany',
                  8: 'Thailand',
                  9: 'Tanzania',
                  10: 'France',
                  11: 'Italy',
                  12: 'Kenya',
                  13: 'Myanmar',
                  14: 'Colombia',
                  15: 'Uganda',
                  16: 'Spain',
                  17: 'Spain',
                  18: 23,
                  19: 24,
                  20: 25, }

print(f"Max value is: {max(dict_duplicate.values(), key=str)}")
print(f"Min value is {min(dict_duplicate.values(), key=str)}")
