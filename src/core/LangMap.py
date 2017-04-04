import json
import datetime


class LangMap:

    def __init__(self):
        LangMap.log(self, "__init__", "Initiated...")

        self.english_to_bengali = self.load_json('../assets/jsons/english_to_bangla_map.json')

        LangMap.log(self, "__init__", "Json parsed!")
        print(self.english_to_bengali)

    def load_json(self, json_path):
        LangMap.log(self, "load_json", "called...")
        with open(json_path) as letter_map_file:
            return json.load(letter_map_file)

    @staticmethod
    def log(class_name, method_name, message):
        log_msg = "["+str(datetime.datetime.now())+"]"
        log_msg += "[" + class_name.__class__.__name__ + "][" + method_name + "] "
        log_msg += message
        print(log_msg)

langMap = LangMap()