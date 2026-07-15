from models.student import Student
from models.user import User

from services.student_service import StudentService
from services.login_service import LoginService

from utils.validation import Validation


def main():

    login_service = LoginService()

    print("=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    user = User(username, password)

    if not login_service.login(user):
        print("\nInvalid Username or Password.")
        return

    print("\nLogin Successful!")

    student_service = StudentService()

    while True:

        print("\n" + "=" * 45)
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=" * 45)

        try:
            choice = int(input("Enter Choice : "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # ---------------- Add Student ----------------

        if choice == 1:

            roll_no = input("Roll Number : ")
            name = input("Student Name : ")

            try:
                age = int(input("Age : "))
            except ValueError:
                print("Age must be a number.")
                continue

            gender = input("Gender : ")
            branch = input("Branch : ")
            email = input("Email : ")
            phone = input("Phone : ")

            try:
                cgpa = float(input("CGPA : "))
            except ValueError:
                print("CGPA must be numeric.")
                continue

            if not Validation.validate_age(age):
                print("Age should be between 16 and 60.")
                continue

            if not Validation.validate_email(email):
                print("Invalid Email Address.")
                continue

            if not Validation.validate_phone(phone):
                print("Phone number must contain 10 digits.")
                continue

            if not Validation.validate_cgpa(cgpa):
                print("CGPA should be between 0 and 10.")
                continue

            student = Student(
                roll_no,
                name,
                age,
                gender,
                branch,
                email,
                phone,
                cgpa
            )

            student_service.add_student(student)

        # ---------------- Display Students ----------------

        elif choice == 2:

            student_service.display_students()

        # ---------------- Search Student ----------------

        elif choice == 3:

            roll_no = input("Enter Roll Number : ")
            student_service.search_student(roll_no)

        # ---------------- Update Student ----------------

        elif choice == 4:

            roll_no = input("Enter Roll Number : ")

            phone = input("New Phone Number : ")

            try:
                cgpa = float(input("New CGPA : "))
            except ValueError:
                print("Invalid CGPA.")
                continue

            if not Validation.validate_phone(phone):
                print("Invalid Phone Number.")
                continue

            if not Validation.validate_cgpa(cgpa):
                print("Invalid CGPA.")
                continue

            student_service.update_student(
                roll_no,
                phone,
                cgpa
            )

        # ---------------- Delete Student ----------------

        elif choice == 5:

            roll_no = input("Enter Roll Number : ")
            student_service.delete_student(roll_no)

        # ---------------- Exit ----------------

        elif choice == 6:

            print("\nThank You for Using Student Management System.")
            break

        else:

            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()
