import data_access


# Add student to dictionary
def add_student(name, age, grade):
    students = data_access.get_dict()
    if name not in students:
        students[name] = {'age': age, 'grade': grade}
        data_access.save_dict(students)
        print(f"Student {name} has been added\n")
    else:
        print(f"Student {name} already exists\n")


# Delete student from dictionary
def delete_student(name):
    students = data_access.get_dict()
    if name not in students:
        print(f"Student {name} not found\n")
    else:
        del students[name]
        data_access.save_dict(students)
        print(f"Student {name} has been deleted\n")


# Search student by name from dictionary
def search_student(name):
    students = data_access.get_dict()
    print(f"{student_info(name,students)}\n")


# Print student's information
def student_info(name, students):
    if name not in students:
        return f"Student {name} not found"
    else:
        return f"Name: {name}, " f"Age: {students[name]['age']}, " f"Grade: {students[name]['grade']}"


# Print list of students' information
def print_list():
    students = data_access.get_dict()
    if not students:
        print("There's no student in the database")
    else:
        print()
        for student in students:
            print(student_info(student, students))
        print()
