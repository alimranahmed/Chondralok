from src.core.LangMap import langMap


class Eng2BanMap:
    def __init__(self):
        self.lang_map = langMap

    def get_bengali_character(self, english_character, last_char=' '):
        if english_character not in self.lang_map.eng_to_ban_map:
            return english_character
        if self.lang_map.eng_to_ban_map[english_character]['type'] == 'vowel':
            if last_char is ' ':
                print('last is space')
                return self.lang_map.eng_to_ban_map[english_character]['replace']
            else:
                print('last is not space')
                return self.lang_map.eng_to_ban_map[english_character]['short_form']
        else:
            return self.lang_map.eng_to_ban_map[english_character]['replace']
