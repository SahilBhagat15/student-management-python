import re


class Validation:

    @staticmethod
    def validate_email(email):

        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        return re.match(pattern, email)

    @staticmethod
    def validate_phone(phone):

        pattern = r'^[6-9]\d{9}$'

        return re.match(pattern, phone)

    @staticmethod
    def validate_age(age):

        return 16 <= age <= 60

    @staticmethod
    def validate_cgpa(cgpa):

        return 0 <= cgpa <= 10