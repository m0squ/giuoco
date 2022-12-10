# External modules #
import json

# Internal modules #
from utils.json_utils import read_json


settings_json_path = "json/settings.json"
settings_json = read_json(settings_json_path)
settings_defaults_json = read_json("json/settings_defaults.json")
for setting_key in settings_json:
    globals()[setting_key] = settings_json[setting_key]


def write_setting(key: str, value: str):
    global settings_json, settings_json_path
    settings_json[key] = value
    with open(settings_json_path, "w") as file:
        json.dump(settings_json, file)
