# Student Management System with File Storage (JSON)

import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

students = load_students()

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    dept = input("Enter Department: ")

    student = {
        "name": name,
        "roll": roll,
        "dept": dept
    }

    students.append(student)
    save_students(students)
    print("Student added and saved successfully!")

def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No students found.")
        return

    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Roll: {student['roll']}, Dept: {student['dept']}")

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")

    for student in students:
        if student["roll"] == roll:
            print("Student Found:")
            print(f"Name: {student['name']}")
            print(f"Roll: {student['roll']}")
            print(f"Dept: {student['dept']}")
            return

    print("Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")

    for student in students:
        if student["roll"] == roll:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
