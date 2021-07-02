import data_access


# Add student to dictionary. Return True if the student is added and saved,
# return False if the student already exists
def add_student(name, age, grade):
    students = data_access.get_dict()
    if name not in students:
        students[name] = {'age': age, 'grade': grade}
        data_access.save_dict(students)
        return True
    else:
        return False


# Delete student from dictionary. Return True if the student is removed and saved,
# return False if the student is not in the dictionary
def delete_student(name):
    students = data_access.get_dict()
    if name not in students:
        return False
    else:
        del students[name]
        data_access.save_dict(students)
        return True


# Print all students with their information
def print_students():
    str = ''
    students = data_access.get_dict()
    if not students:
        return "No students yet in the database"
    for student in students:
        str += f"Name: {student}, " \
               f"Age: {students[student]['age']}, " \
               f"Grade: {students[student]['grade']}\n"
    print(str)
