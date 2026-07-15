import mysql.connector
from config import HOST, USER, PASSWORD, DATABASE


class Database:

    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=HOST,
                user=USER,
                password=PASSWORD,
                database=DATABASE
            )

            if self.connection.is_connected():
                print("Database Connected Successfully")

            return self.connection

        except mysql.connector.Error as e:
            print("Database Connection Error:", e)

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database Connection Closed")