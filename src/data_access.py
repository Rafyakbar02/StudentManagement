import json


# Open or create file called students.txt and return a dictionary whether it is filled or empty
def get_dict():
    d = {}
    try:
        with open("students.json", "r") as json_file:
            d = json.load(json_file)
    except FileNotFoundError:
        pass
    return d


# Save dictionary to students.txt with json
def save_dict(data):
    with open("students.json", "w") as outfile:
        json.dump(data, outfile, sort_keys=True)
