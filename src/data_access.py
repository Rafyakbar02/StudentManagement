import json


# Open or create file called students.txt and return a dictionary whether it is filled or empty
def open_file():
    d = {}
    try:
        with open("students.json", "r") as json_file:
            d = json.load(json_file)
    except FileNotFoundError:
        pass
    return d


# Save dictionary to students.txt with json
def save_file(data):
    with open("students.json", "w") as outfile:
        json.dump(data, outfile, sort_keys=True)
