import sys
import student_list


# Add student to database if the student is not in the database yet
def add_student():
    while True:
        age = 0
        name = input("\nEnter student's name: ")
        while True:
            try:
                age = int(input("Enter student's age: "))
                if age <= 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input!\n")
        grade = input("Enter student's grade level: ")
        student_list.add_student(name, age, grade)
        if repeat("add"):
            continue
        else:
            break


# Delete student from database if the student is already in the database yet
def delete_student():
    while True:
        name = input("\nEnter student's name: ")
        answer = input(f"Are you sure you want to delete {name}? (Y/n) ")
        if answer == "Y":
            student_list.delete_student(name)
        elif answer == "n":
            pass
        else:
            print("Invalid input!\n")
        if repeat("delete"):
            continue
        else:
            break


def search_student():
    while True:
        name = input("\nEnter student's name: ")
        student_list.search_student(name)
        if repeat("search"):
            continue
        else:
            break


def repeat(process):
    while True:
        answer = input(f"Do you want to {process} another student? (Y/n) ")
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            print()
            return False
        else:
            print("Invalid input!\n")


# Print list of students sorted by name
def list_of_students():
    student_list.print_list()


choice = 0
ui = {1: {'process': 'Add student', 'function': add_student},
      2: {'process': 'Delete student', 'function': delete_student},
      3: {'process': 'Search student', 'function': search_student},
      4: {'process': 'List of students', 'function': list_of_students},
      5: {'process': 'Quit', 'function': sys.exit}}

while True:
    print("Welcome to Student Information Manager!")
    for menu in ui:
        print(f"{menu} - {ui[menu]['process']}")
    try:
        choice = int(input("Enter a number: "))
        if choice in ui:
            ui[choice]['function']()
        else:
            raise ValueError
    except ValueError:
        print("Invalid input!\n")
