import json
import os


class JSONManager:
    def save_json(self, json_data, file_name, directory_name=""):
        os.makedirs(directory_name, exist_ok=True)
        with open(f"{directory_name}/{file_name}", "w") as json_file:
            json.dump(json_data, json_file)
