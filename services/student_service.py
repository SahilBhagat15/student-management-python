from database.db import Database


class StudentService:

    def __init__(self):
        self.db = Database()

    # ------------------- Add Student -------------------

    def add_student(self, student):

        conn = self.db.connect()

        if conn is None:
            return

        cursor = conn.cursor()

        query = """
        INSERT INTO students
        (roll_no, name, age, gender, branch, email, phone, cgpa)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            student.get_roll_no(),
            student.name,
            student.age,
            student.gender,
            student.get_branch(),
            student.get_email(),
            student.get_phone(),
            student.get_cgpa()
        )

        try:
            cursor.execute(query, values)
            conn.commit(),
            print("\nStudent Added Successfully.")

        except Exception as e:
            print("\nError :", e)

        finally:
            cursor.close()
            self.db.close()

    # ------------------- Display Students -------------------

    def display_students(self):

        conn = self.db.connect()

        if conn is None:
            return

        cursor = conn.cursor()

        query = "SELECT * FROM students"

        cursor.execute(query)

        students = cursor.fetchall()

        if len(students) == 0:
            print("\nNo Student Found.")
        else:
            print("\n========== STUDENT LIST ==========")

            for row in students:
                print("--------------------------------------")
                print("ID      :", row[0])
                print("Roll No :", row[1])
                print("Name    :", row[2])
                print("Age     :", row[3])
                print("Gender  :", row[4])
                print("Branch  :", row[5])
                print("Email   :", row[6])
                print("Phone   :", row[7])
                print("CGPA    :", row[8])

        cursor.close()
        self.db.close()

    # ------------------- Search Student -------------------

    def search_student(self, roll_no):

        conn = self.db.connect()

        if conn is None:
            return

        cursor = conn.cursor()

        query = "SELECT * FROM students WHERE roll_no=%s"

        cursor.execute(query, (roll_no,))

        student = cursor.fetchone()

        if student:
            print("\nStudent Found")
            print("---------------------------")
            print("Roll No :", student[1])
            print("Name    :", student[2])
            print("Age     :", student[3])
            print("Gender  :", student[4])
            print("Branch  :", student[5])
            print("Email   :", student[6])
            print("Phone   :", student[7])
            print("CGPA    :", student[8])

        else:
            print("\nStudent Not Found.")

        cursor.close()
        self.db.close()

    # ------------------- Delete Student -------------------

    def delete_student(self, roll_no):

        conn = self.db.connect()

        if conn is None:
            return

        cursor = conn.cursor()

        query = "DELETE FROM students WHERE roll_no=%s"

        cursor.execute(query, (roll_no,))

        conn.commit(),

        if cursor.rowcount > 0:
            print("\nStudent Deleted Successfully.")
        else:
            print("\nStudent Not Found.")

        cursor.close()
        self.db.close()

    # ------------------- Update Student -------------------

    def update_student(self, roll_no, phone, cgpa):

        conn = self.db.connect()

        if conn is None:
            return

        cursor = conn.cursor()

        query = """
        UPDATE students
        SET phone=%s, cgpa=%s
        WHERE roll_no=%s
        """

        cursor.execute(query, (phone, cgpa, roll_no))

        conn.commit(),

        if cursor.rowcount > 0:
            print("\nStudent Updated Successfully.")
        else:
            print("\nStudent Not Found.")

        cursor.close()
        self.db.close()