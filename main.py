from student import Students

student = Students()


# Add student to database if the student is not in the database yet
def add_student():
    name = input("\nEnter student's name: ")
    age = int(input("Enter student's age: "))
    grade = input("Enter student's grade level: ")
    if student.add_student(name, age, grade):
        print(f"Student {name} has been added")
    else:
        print(f"Student {name} already exists")


# Delete student from database if the student is already in the database yet
def delete_student():
    name = input("\nEnter student's name: ")
    answer = input(f"Are you sure you want to delete {name}? (Y/n")
    if answer == "Y":
        if student.delete_student(name):
            print(f"Student {name} has been deleted")
        else:
            print(f"Student {name} not found")
    elif answer == "n":
        pass
    else:
        print("Wrong input!")


# Print list of students sorted by name
def list_of_students():
    print(student)


choice = 0
print("Welcome to Student Information Manager!")

while choice != 4:
    print("\nWhat can we help you with?\n"
          "1 - Add student\n"
          "2 - Delete student\n"
          "3 - List of students\n"
          "4 - Quit")
    choice = int(input("Enter a number: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        list_of_students()
    else:
        print("Goodbye!")
