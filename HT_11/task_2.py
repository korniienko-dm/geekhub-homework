"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде
приймати якісь аргументи, які зберігатиме в відповідні змінні.
- Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
- Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут
  profession (його не має інсувати під час ініціалізації).
"""

class Person:
    """
    A class representing a person with attributes such as name, age, and profession.

    Attributes:
    - name (str): The name of the person.
    - age (int): The age of the person.

    Methods:
    - show_age(): Display the age of the person.
    - print_name(): Print the name of the person.
    - show_all_information(): Display all available information about the person.
    """

    def __init__(self, name: str, age: str):
        """
        Initialize a Person instance with a given name and age.

        Parameters:
        - name (str): The name of the person.
        - age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def show_all_information(self):
        return vars(self)


old_employee = Person(name='Ivan', age=33)
old_employee.profession = "Builder"

new_employee = Person(name='Denis', age=44)
new_employee.profession = "Mechanic"

print(old_employee.get_name(), old_employee.get_age(), old_employee.show_all_information())
print(new_employee.get_name(), new_employee.get_age(), new_employee.show_all_information())
