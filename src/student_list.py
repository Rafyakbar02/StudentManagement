import data_access


# Add student to dictionary
def add_student(name, age, grade):
    students = data_access.get_dict()
    if name not in students:
        students[name] = {'age': age, 'grade': grade}
        data_access.save_dict(students)
        return True
    else:
        return False


# Delete student from dictionary
def delete_student(name):
    students = data_access.get_dict()
    if name not in students:
        return False
    else:
        del students[name]
        data_access.save_dict(students)
        return True


# Search student by name from dictionary
def search_student(name):
    students = data_access.get_dict()
    if name not in students:
        print(f"Student {name} not found\n")
    else:
        print(f"Name: {name}, " f"Age: {students[name]['age']}, " f"Grade: {students[name]['grade']}\n")


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
