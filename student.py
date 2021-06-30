import data_access
from collections import OrderedDict


# Represents a dictionary of students that is sorted by name.
class Students:

    # Create an ordered dictionary of students from a filled or empty .txt file
    def __init__(self):
        self.students = OrderedDict(data_access.open_file())

    # Add student to dictionary. Return True if the student is added and saved,
    # return False if the student already exists
    def add_student(self, name, age, grade):
        self.students = data_access.open_file()
        if name not in self.students:
            self.students[name] = {'age': age, 'grade': grade}
            data_access.save_file(self.students)
            return True
        else:
            return False

    # Delete student from dictionary. Return True if the student is removed and saved,
    # return False if the student is not in the dictionary
    def delete_student(self, name):
        self.students = data_access.open_file()
        if name not in self.students:
            return False
        else:
            del self.students[name]
            data_access.save_file(self.students)
            return True

    # String representation of Students class
    def __str__(self):
        str = ""
        if not self.students:
            return "No students yet in the database"
        for student in self.students:
            str += f"Name: {student}, " \
                   f"Age: {self.students[student]['age']}, " \
                   f"Grade: {self.students[student]['grade']}\n"
        return str
