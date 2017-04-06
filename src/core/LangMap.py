from src.core.Utility import Utility


class LangMap:

    def __init__(self):
        self.english_to_bengali = Utility.load_json('../assets/jsons/english_to_bangla_map.json')
        print(self.english_to_bengali)

langMap = LangMap()