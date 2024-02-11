#!/usr/bin/python3
""" Base class """
import json
import os
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        dict_objs = []
        for i in range(len(list_objs)):
            dict_objs.append(list_objs[i].to_dictionary())
        json_string = cls.to_json_string(dict_objs)
        with open(cls.__name__ + ".json", "w", encoding="UTF8") as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        c1 = cls(1000, 1000)
        c1.update(**dictionary)
        return c1

    @classmethod
    def load_from_file(cls):
        list_instances = []
        if not os.path.isfile(cls.__name__ + ".json"):
            return list_instances
        with open(cls.__name__ + ".json", "r", encoding="UTF8") as f:
            json_string = f.read()
        dic_instances = cls.from_json_string(json_string)
        for instance in dic_instances:
            list_instances.append(cls.create(**instance))
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        dict_objs = []
        for i in range(len(list_objs)):
            dict_objs.append(list_objs[i].to_dictionary())
        json_string = cls.to_json_string(dict_objs)
        with open(cls.__name__ + ".json", "w", encoding="UTF8") as csvfile:
            dict_writer = csv.writer(csvfile)
            dict_writer.writerow(dict_objs)

    @classmethod
    def load_from_file_csv(cls):
        list_instances = []
        if not os.path.isfile(cls.__name__ + ".csv"):
            return list_instances
        with open(cls.__name__ + ".csv", "r", encoding="UTF8") as f:
            reader = csv.reader(f)
            for row in f:
                print(', '.join(row) )
