import json


class Eng2BanMap:

    def __init__(self):
        with open('bengali_to_english.json') as letter_map_file:
            bengali_to_english = json.load(letter_map_file)

        self.english_to_bengali = {value: key for key, value in bengali_to_english.items()}

    def get_bengali_character(self, english_character):
        return self.english_to_bengali[english_character]
