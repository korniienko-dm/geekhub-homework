"""
3. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""

class CompanyEmployeer:
    """
    Representing an employee in a company.
    """
    class_count_instances = 0

    def __init__(self, first_name, last_name, age, working_position):
        """
        Initializes a new instance of the CompanyEmployee class.
        """
        CompanyEmployeer.class_count_instances += 1

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.working_position = working_position


employeer_id_123 = CompanyEmployeer(first_name='John', last_name='Malkovitch', age=44, working_position='Engineer')
employeer_id_124 = CompanyEmployeer(first_name='Ryan', last_name='Johnson', age=26, working_position='Security guard')
employeer_id_125 = CompanyEmployeer(first_name='Jeremiah', last_name='Gate', age=31, working_position='Economist')
employeer_id_126 = CompanyEmployeer(first_name='Daniel', last_name='Mitchell', age=36, working_position='Electrician')

print(f"Number of created instances of class 'CompanyEmployeer' is: {CompanyEmployeer.class_count_instances}")
