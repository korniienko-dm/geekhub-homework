"""
Taks_5:
Write a script to remove values duplicates from dictionary.
Feel free to hardcode your dictionary.
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
                  18: 'Canada',
                  19: 'Canada',
                  20: 'Canada'}

set_unique_value = set(dict_duplicate.values())
dict_uniqie = dict()

for unique_value in set_unique_value:

    for key in dict_duplicate:
        if unique_value == dict_duplicate[key]:
            dict_uniqie[key] = dict_duplicate[key]
            break

print(dict_uniqie)
