"""
Create 'list'-like object, but index starts from 1 and index of 0 raises error.
Тобто це повинен бути клас, який буде поводити себе так, як list
(маючи основні методи), але індексація повинна починатись із 1
"""

class AlternativeList:
    """
    An alternative list implementation where indexing starts from 1 instead of 0.
    """
    def __init__(self, *args):
        self._data = list(args)

    def __getitem__(self, index):
        """
        Retrieves the element at the specified index.
        """
        if index == 0:
            raise IndexError("Index starts from 1, not 0")
        return self._data[index - 1]

    def __setitem__(self, index, value):
        """
        Sets the element at the specified index to the given value.
        """
        if index == 0:
            raise IndexError("Index starts from 1, not 0")
        self._data[index - 1] = value

    def __delitem__(self, index):
        """
        Deletes the element at the specified index.
        """
        if index == 0:
            raise IndexError("Index starts from 1, not 0")
        del self._data[index - 1]

    def __len__(self):
        """
        Returns the number of elements in the AlternativeList.
        """
        return len(self._data)

    def __repr__(self):
        """
        Returns a string representation of the AlternativeList.
        """
        return repr(self._data)


my_new_list = AlternativeList(10, 20, 30, 40, 50)
print(my_new_list[1])
print(my_new_list[3])

my_new_list[2] = 25
print(my_new_list)

del my_new_list[4]
print(my_new_list)

print(len(my_new_list))
