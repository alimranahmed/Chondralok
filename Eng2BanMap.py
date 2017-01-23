import json


class Eng2BanMap:

    def __init__(self):
        with open('draft_map.json') as letter_map_file:
            bengali_to_english = json.load(letter_map_file)

        self.english_to_bengali = {value: key for key, value in bengali_to_english.items()}

    def ge_bengali_character(self, english_character):
        return self.english_to_bengali[english_character]


map = Eng2BanMap()
print(map.ge_bengali_character("k"))
