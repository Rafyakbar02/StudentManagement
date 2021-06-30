import json
from json.decoder import JSONDecodeError


# Open or create file called students.txt and return a dictionary whether it is filled or empty
def open_file():
    d = {}
    with open("students.txt") as json_file:
        try:
            d = json.load(json_file)
        except JSONDecodeError:
            pass
    return d


# Save dictionary to students.txt with json
def save_file(data):
    with open("students.txt", "w") as outfile:
        json.dump(data, outfile)