from models.person import Person


class Student(Person):

    def __init__(self,
                 roll_no,
                 name,
                 age,
                 gender,
                 branch,
                 email,
                 phone,
                 cgpa):

        super().__init__(name, age, gender)

        self.__roll_no = roll_no
        self.__branch = branch
        self.__email = email
        self.__phone = phone
        self.__cgpa = cgpa

    # Getter Methods

    def get_roll_no(self):
        return self.__roll_no

    def get_branch(self):
        return self.__branch

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_cgpa(self):
        return self.__cgpa

    # Setter Methods

    def set_branch(self, branch):
        self.__branch = branch

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_cgpa(self, cgpa):
        self.__cgpa = cgpa

    def display_student(self):

        print("\nStudent Details")

        print("Roll No :", self.__roll_no)
        print("Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)
        print("Branch :", self.__branch)
        print("Email :", self.__email)
        print("Phone :", self.__phone)
        print("CGPA :", self.__cgpa)