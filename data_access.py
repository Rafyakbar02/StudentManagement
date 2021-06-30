import json
from json.decoder import JSONDecodeError


def open_file():
    d = {}
    with open("students.txt") as json_file:
        try:
            d = json.load(json_file)
        except JSONDecodeError:
            pass
    return d


def save_file(data):
    with open("students.txt", "w") as outfile:
        json.dump(data, outfile)