"""
Taks_2:
Write a script to remove an empty elements from a list.
Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
"""


lst = [(),
       ('hey'),
       ('',),
       ('ma', 'ke', 'my'),
       [''],
       {},
       ['d', 'a', 'y'],
       '',
       []]

lst_without_empty_elem = list()

for elem_lst in lst:
    if elem_lst:
        lst_without_empty_elem.append(elem_lst)

lst = lst_without_empty_elem

print(lst)
