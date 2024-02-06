#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dic = self.__dict__
            return {key: dic[key] for key in attrs if key in dic}
        return self.__dict__

    def reload_from_json(self, json):
        dic = self.__dict__
        for key in json.keys():
            dic[key] = json[key]
