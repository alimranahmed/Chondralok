from src.core.Utility import Utility


class LangMap:

    def __init__(self):
        json_path = '../assets/json/english_to_bangla_map.json'
        self.english_to_bengali = Utility.load_json(json_path)
        print(self.english_to_bengali)

langMap = LangMap()