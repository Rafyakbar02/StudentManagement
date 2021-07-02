import student


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
        if student.add_student(name, age, grade):
            print(f"Student {name} has been added\n")
        else:
            print(f"Student {name} already exists\n")
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
            if student.delete_student(name):
                print(f"Student {name} has been deleted\n")
            else:
                print(f"Student {name} not found\n")
        elif answer == "n":
            pass
        else:
            print("Invalid input!\n")
        if repeat("delete"):
            continue
        else:
            break


def repeat(process):
    while True:
        answer = input(f"Do you want to {process} another student? (Y/n) ")
        if answer.upper() == 'Y':
            return True
        elif answer.upper() == 'N':
            print('\n')
            return False
        else:
            print("Invalid input!\n")


# Print list of students sorted by name
def list_of_students():
    print(student)


choice = 0
print("Welcome to Student Information Manager!")

while True:
    print("What can we help you with?\n"
          "1 - Add student\n"
          "2 - Delete student\n"
          "3 - List of students\n"
          "4 - Quit")
    try:
        choice = int(input("Enter a number: "))
        if choice == 1:
            add_student()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            list_of_students()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input!\n")
