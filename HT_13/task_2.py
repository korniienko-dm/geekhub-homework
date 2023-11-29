"""
2. Створіть за допомогою класів та продемонструйте свою реалізацію шкільної
бібліотеки (включіть фантазію). Наприклад вона може містити класи:
Person, Teacher, Student, Book, Shelf, Author, Category і.т.д.
"""
import sqlite3
from datetime import date
from pathlib import Path

WORK_BASE_DIR = Path(__file__).resolve().parent
WORK_DB_NAME = 'task_2_file/school_library.db'

class Administrator:
    """
    A class representing an administrator of the library management system.
    
    Attributes:
    - db_path (str): The path to the SQLite database file.
    - conn (sqlite3.Connection): SQLite database connection.
    - cursor (sqlite3.Cursor): SQLite database cursor.

    Methods:
    - issue_book:
      Issues a book to a student and updates the database accordingly.

    - return_book:
      Returns a book from a student and updates the database accordingly.

    - register_student:
      Registers a new student in the system.

    - delete_student:
      Deletes a student from the system.

    - add_book:
      Adds a new book to the system.

    - delete_book:
      Deletes a book from the system.

    - display_menu:
      Displays the main menu of the library management system.

    - handle_menu_choice:
      Handles user input based on the selected menu option.

    - run:
      Runs the library management system, continuously displaying the menu and processing user input.

    - __del__:
      Closes the database connection when the Administrator object is deleted.
    """
    def __init__(self, db_path):
        """
        Initializes the Administrator class with the provided database path. 
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()


    def issue_book(self, student_id, book_id):
        """
        Issues a book to a student and updates the database accordingly.
        """
        self.cursor.execute("SELECT book_status FROM books_collection WHERE book_id = ?", (book_id,))
        status = self.cursor.fetchone()
        if status and status[0] == 'available':
            self.cursor.execute("UPDATE books_collection SET book_status = 'issued' WHERE book_id = ?", (book_id,))
            self.cursor.execute("INSERT INTO issued_books_manage (issue_date, student_id, book_id) VALUES (?, ?, ?)",
                                (date.today(), student_id, book_id))
            self.cursor.execute("SELECT book_name FROM books_collection WHERE book_id = ?", (book_id,))
            book_name = self.cursor.fetchone()[0]
            self.conn.commit()
            print(f'Book: "{book_name}" issued successfully.')
        else:
            print("The book is not available for issue.")


    def return_book(self, student_id, book_id):
        """
        Returns a book from a student and updates the database accordingly.
        """
        self.cursor.execute("SELECT book_status FROM books_collection WHERE book_id = ?", (book_id,))
        status = self.cursor.fetchone()
        if status and status[0] == 'issued':
            self.cursor.execute("UPDATE books_collection SET book_status = 'available' WHERE book_id = ?", (book_id,))
            self.cursor.execute("INSERT INTO return_books_manage (return_date, student_id, book_id) VALUES (?, ?, ?)",
                                (date.today(), student_id, book_id))
            self.cursor.execute("SELECT book_name FROM books_collection WHERE book_id = ?", (book_id,))
            book_name = self.cursor.fetchone()[0]
            self.conn.commit()
            print(f'Book: "{book_name}" returned successfully.')
        else:
            print("The book was not issued and therefore cannot be returned.")


    def register_student(self, first_name, last_name, student_class, phone_number, school_student_id):
        """
        Registers a new student in the system.
        """
        self.cursor.execute("INSERT INTO students (student_first_name, student_last_name, student_class, "
                            "student_phone_number, school_student_id) VALUES (?, ?, ?, ?, ?)",
                            (first_name, last_name, student_class, phone_number, school_student_id))
        self.conn.commit()
        print(f'Student: "{first_name} {last_name}" successfully registered.')


    def delete_student(self, student_id):
        """
        Deletes a student from the system.
        """
        self.cursor.execute("SELECT student_first_name FROM students WHERE student_id = ?", (student_id,))
        student_first_name = self.cursor.fetchone()
        self.cursor.execute("SELECT student_last_name FROM students WHERE student_id = ?", (student_id,))
        student_last_name = self.cursor.fetchone()
        if student_first_name and student_first_name[0]:
            self.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
            self.conn.commit()
            print(f"Student: {student_first_name[0]} {student_last_name[0]} deleted successfully.")
        else:
            print(f'Error: Student with ID: "{student_id}" is not registered in the system!')


    def add_book(self, book_name, book_author, isbn, book_status, category_id):
        """
        Adds a new book to the system.
        """
        self.cursor.execute("INSERT INTO books_collection (book_name, book_author, isbn, book_status, category_id) "
                            "VALUES (?, ?, ?, ?, ?)",
                            (book_name, book_author, isbn, book_status, category_id))
        self.conn.commit()
        print(f'Book: "{book_name}" added successfully.')


    def delete_book(self, book_id):
        """
        Deletes a book from the system. 
        """
        self.cursor.execute("SELECT book_name FROM books_collection WHERE book_id = ?", (book_id,))
        book_name = self.cursor.fetchone()
        if book_name and book_name[0]:
            self.cursor.execute("DELETE FROM books_collection WHERE book_id = ?", (book_id,))
            self.conn.commit()
            print(f'Book: "{book_name[0]}" successfully deleted.')
        else:
            print(f'Book with ID: "{book_id}" was not found in the library.')


    def display_menu(self):
        """
        Displays the main menu of the library management system.
        """
        menu_elements = [
            '\n-----------------------------------\n',
             '|            Welcome to            |\n',
             '|   "Library management system"    |\n',
             '------------------------------------\n',
             'Please select your action:\n\n',
             '[1] Issue book\n',
             '[2] Return book\n',
             '[3] Student registration\n',
             '[4] Removing student\n',
             '[5] Add new book\n',
             '[6] Delete book \n\n',
             '[0] Exit program']

        return "".join(menu_elements)


    def handle_menu_choice(self, choice):
        """
        Handles user input based on the selected menu option.
        """
        # [1] Issue book
        if choice == '1':
            student_id = input("Enter student ID: ")
            book_id = input("Enter book ID: ")
            self.issue_book(int(student_id), int(book_id))
            input("\nPress Enter to continue...")
        # [2] Return book
        elif choice == '2':
            student_id = input("Enter student ID: ")
            book_id = input("Enter book ID: ")
            self.return_book(int(student_id), int(book_id))
            input("\nPress Enter to continue...")
        # [3] Student registration
        elif choice == '3':
            first_name = input("Enter student name: ")
            last_name = input("Enter the student's last name: ")
            student_class = input("Enter student class: ")
            phone_number = input("Enter the student's phone number: ")
            school_student_id = input("Enter student ID: ")
            self.register_student(first_name, last_name, student_class, phone_number, int(school_student_id))
            input("\nPress Enter to continue...")
        # [4] Removing student
        elif choice == '4':
            student_id = input("Enter the student ID to delete: ")
            self.delete_student(int(student_id))
            input("\nPress Enter to continue...")
        # [5] Add new book
        elif choice == '5':
            book_name = input("Enter the title of the book: ")
            book_author = input("Enter the author of the book: ")
            isbn = input("Enter the book's ISBN number: ")
            book_status = input("Enter book status (available/issued): ")
            category_id = input("Enter the book category ID: ")
            self.add_book(book_name, book_author, int(isbn), book_status, int(category_id))
            input("\nPress Enter to continue...")
        # [6] Delete book
        elif choice == '6':
            book_id = input("Enter the book ID to delete: ")
            self.delete_book(int(book_id))
            input("\nPress Enter to continue...")
        # [0] Exit program
        elif choice == '0':
            print("Exit the program.")
            return False
        else:
            print("Invalid input. Please select an action from the list.")
        return True


    def run(self):
        """
        Runs the library management system, continuously displaying the menu and processing user input.
        """
        while True:
            print(self.display_menu())
            user_choice = input("Your choice: ")
            if not self.handle_menu_choice(user_choice):
                break


    def __del__(self):
        """
        Closes the database connection when the Administrator object is deleted. 
        """
        self.conn.close()


if __name__ == "__main__":
    librarian_administrator = Administrator(db_path=WORK_BASE_DIR / WORK_DB_NAME)
    librarian_administrator.run()






























