import json


class Eng2BanMap:
    def __init__(self):
        print("JSON parsing...")
        with open('bengali_to_english.json') as letter_map_file:
            self.english_to_bengali = json.load(letter_map_file)
        print(self.english_to_bengali)
        print('JSON parsed')

    def get_bengali_character(self, english_character, last_char=' '):
        if english_character not in self.english_to_bengali:
            return english_character
        if type(self.english_to_bengali[english_character]) is list:
            if last_char is ' ':
                print('last is space')
                return self.english_to_bengali[english_character][0]
            else:
                print('last is not space')
                return self.english_to_bengali[english_character][1]
        else:
            return self.english_to_bengali[english_character]
