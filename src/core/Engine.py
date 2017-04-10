from src.core.LangMap import langMap


class Eng2BanMap:
    def __init__(self):
        self.eng_to_ban_map = langMap.eng_to_ban_map

    def get_bengali_character(self, english_character, last_eng_char=' '):
        print(last_eng_char+english_character)
        # letters with more than one character
        # TODO create separate method
        if last_eng_char+english_character in self.eng_to_ban_map:
            print('is in map')
            if self.eng_to_ban_map[last_eng_char+english_character]['type'] == 'vowel':
                if last_eng_char is ' ':
                    print('last is space')
                    return self.eng_to_ban_map[last_eng_char+english_character]['replace']
                else:
                    print('last is not space')
                    return self.eng_to_ban_map[last_eng_char+english_character]['short_form']
            else:
                return self.eng_to_ban_map[last_eng_char+english_character]['replace']
        # TODO separate this method also
        if english_character not in self.eng_to_ban_map:
            return english_character
        if self.eng_to_ban_map[english_character]['type'] == 'vowel':
            if last_eng_char is ' ':
                print('last is space')
                return self.eng_to_ban_map[english_character]['replace']
            else:
                print('last is not space')
                return self.eng_to_ban_map[english_character]['short_form']
        else:
            return self.eng_to_ban_map[english_character]['replace']
