import json


def read_json(path: str):
    with open(path) as file:
        print(f"JSON file {path} loaded successfully")
        return json.load(file)
