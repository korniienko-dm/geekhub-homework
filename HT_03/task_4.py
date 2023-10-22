"""
Taks_4:
Write a script that combines three dictionaries by updating the first one.
"""


dict_1 = {1: 'one',
                  2: 'two',
                  3: 'three',
                  4: 'four',
                  5: 'five'}

dict_2 = {6: 'six',
          7: 'seven',
          8: 'eight',
          9: 'nine',
          10: 'ten'}


dict_3 = {11: 'eleven',
          12: 'twelve',
          13: 'thirteen',
          14: 'fourteen',
          15: 'fifteen'}

list_dictionary = [dict_2, dict_3]
concatenate_dict = dict()

for dictionary in list_dictionary:
    dict_1.update(dictionary)

print(dict_1)
