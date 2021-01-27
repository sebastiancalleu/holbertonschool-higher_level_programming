#!/usr/bin/python3
"""
class to define a base
"""

import json
import csv
import turtle


class Base:
    """
    Base
    clase to define a base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor

        arguments
            id - the id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string
        static method
        convert to json string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file
        class method
        save the json string
        """
        if list_objs is None:
            filename = cls.__name__ + ".json"
            with open(filename, mode="w", encoding="UTF8") as textfile:
                ls = cls.to_json_string(ls)
                textfile.write(dict1)
        else:
            filename = cls.__name__ + ".json"
            ls = []
            for i in range(len(list_objs)):
                ls.append(list_objs[i].to_dictionary())
            with open(filename, mode="w", encoding="UTF8") as textfile:
                dict1 = cls.to_json_string(ls)
                textfile.write(dict1)

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string
        static method to convert
        a json string
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create
        classmethod
        creates a object from a dict
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        else:
            dummy = cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        load_from_file
        classmethod
        load from a json file
        """
        try:
            filename = cls.__name__ + ".json"
            with open(filename, mode="r", encoding="UTF8") as textfile:
                jsonstring = textfile.read()
                lsdicts = cls.from_json_string(jsonstring)

            lsobj = []
            for i in range(len(lsdicts)):
                lsobj.append(cls.create(**lsdicts[i]))
            return lsobj
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save_to_file_csv
        class method
        save to csv file
        """
        if list_objs is None:
            filename = cls.__name__ + ".csv"
            with open(filename, mode="w", encoding="UTF8") as textfile:
                emptyls = csv.writer(textfile)
                empytls.writerow([])
        else:
            filename = cls.__name__ + ".csv"
            ls = []
            for i in range(len(list_objs)):
                ls.append(list_objs[i].to_dictionary())
            with open(filename, mode="w", encoding="UTF8") as textfile:
                dict1 = csv.writer(textfile)
                dict1.writerow(ls)

    @classmethod
    def load_from_file_csv(cls):
        """
        load_from_file_csv
        classmethod
        load a csv file
        """
        try:
            filename = cls.__name__ + ".csv"
            with open(filename, mode="r", encoding="UTF8") as textfile:
                lsdicts = csv.reader(textfile)
                ls = []
                for row in lsdicts:
                    for i in range(len(row)):
                        dist1 = eval(row[i])
                        ls.append(dist1)

            lsobj = []
            for i in range(len(ls)):
                lsobj.append(cls.create(**ls[i]))
            return lsobj
        except Exception:
            return []
