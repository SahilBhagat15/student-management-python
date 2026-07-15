from database.db import Database


class LoginService:

    def __init__(self):
        self.db = Database()

    def login(self, user):

        conn = self.db.connect()

        if conn is None:
            return False

        cursor = conn.cursor()

        query = """
        SELECT *
        FROM users
        WHERE username=%s AND password=%s
        """

        values = (
            user.get_username(),
            user.get_password()
        )

        cursor.execute(query, values)

        result = cursor.fetchone()

        cursor.close()
        self.db.close()

        if result:
            return True

        return False