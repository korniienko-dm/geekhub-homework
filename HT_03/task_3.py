"""
Taks_3:
Write a script to concatenate following dictionaries to create a new one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}
"""


dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}

concatenate_dict = dict()

list_dictionary = [dict_1, dict_2, dict_3]

for dictionary in list_dictionary:
    concatenate_dict.update(dictionary)

print(concatenate_dict)
