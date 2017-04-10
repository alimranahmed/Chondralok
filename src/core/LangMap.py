from src.core.Utility import Utility


class LangMap:

    def __init__(self):
        letter_map_list = Utility.load_json('/var/www/html/Chondralok/src/assets/json/english_to_bangla_map.json')
        self.eng_to_ban_map = self.make_dict(letter_map_list)
        print(self.eng_to_ban_map)

    @staticmethod
    def make_dict(letter_map_list):
        eng_to_ban_map = {}
        for letter in letter_map_list:
            eng_to_ban_map[letter['search_for']] = letter
        return eng_to_ban_map

langMap = LangMap()