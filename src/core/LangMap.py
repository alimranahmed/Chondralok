import json


class LangMap:

    def __init__(self):
        print("JSON parsing...")
        with open('bengali_to_english.json') as letter_map_file:
            self.english_to_bengali = json.load(letter_map_file)
        print(self.english_to_bengali)
        print('JSON parsed')