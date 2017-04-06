import datetime
import json


class Utility:
    @staticmethod
    def log(class_name, method_name, message):
        log_msg = "[" + str(datetime.datetime.now()) + "]"
        log_msg += "[" + class_name.__class__.__name__ + "][" + method_name + "] "
        log_msg += message
        print(log_msg)

    @staticmethod
    def load_json(json_path):
        with open(json_path) as letter_map_file:
            return json.load(letter_map_file)