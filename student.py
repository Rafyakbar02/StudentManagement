import data_access
from collections import OrderedDict


class Students:

    def __init__(self):
        self.students = OrderedDict(data_access.open_file())

    def add_student(self, name, age, grade):
        self.students = data_access.open_file()
        if name not in self.students:
            self.students[name] = {'age': age, 'grade': grade}
            data_access.save_file(self.students)
            return True
        else:
            return False

    def delete_student(self, name):
        self.students = data_access.open_file()
        if name not in self.students:
            return False
        else:
            del self.students[name]
            data_access.save_file(self.students)
            return True

    def __str__(self):
        str = ""
        if not self.students:
            return "No students yet in the database"
        for student in self.students:
            str += f"Name: {student}, " \
                   f"Age: {self.students[student]['age']}, " \
                   f"Grade: {self.students[student]['grade']}\n"
        return str
