#!/usr/bin/python3
"""
class that defines a student
"""


class Student:
    """
    Student
    class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor

        arguments
            first_name = first name of the student
            last_name = last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json
        public instance method
        returns a dict description
        """
        return self.__dict__
