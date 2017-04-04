import json
from src.core.Utility import Utility


class LangMap:

    def __init__(self):
        Utility.log(self, "__init__", "Initiated...")

        self.english_to_bengali = self.load_json('../assets/jsons/english_to_bangla_map.json')

        Utility.log(self, "__init__", "Json parsed!")
        print(self.english_to_bengali)

    def load_json(self, json_path):
        Utility.log(self, "load_json", "called...")
        with open(json_path) as letter_map_file:
            return json.load(letter_map_file)

langMap = LangMap()