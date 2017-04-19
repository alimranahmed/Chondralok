from src.core.LangMap import langMap


class Engine:
    def __init__(self):
        self.eng_to_ban_map = langMap.eng_to_ban_map

    def get_ban_char(self, eng_char, last_eng_chars):
        # letters with more than one character
        if last_eng_chars[0]+last_eng_chars[1]+eng_char in self.eng_to_ban_map:
            add_char = self.get_char_to_replace(last_eng_chars[0]+last_eng_chars[1]+eng_char, last_eng_chars[1])
            return {"ban_char": add_char, "replace_count": 2}
        elif last_eng_chars[1]+eng_char in self.eng_to_ban_map:
            add_char = self.get_char_to_replace(last_eng_chars[1] + eng_char, last_eng_chars[1])
            return {"ban_char": add_char, "replace_count": 1}
        else:
            add_char = self.get_char_to_replace(eng_char, last_eng_chars[1])
            return {"ban_char": add_char, "replace_count": 0}

    def get_char_to_replace(self, eng_chars, last_eng_char):
        if eng_chars not in self.eng_to_ban_map:
            return eng_chars

        if self.eng_to_ban_map[eng_chars]['type'] == 'vowel':
            if last_eng_char is ' ' or self.eng_to_ban_map[last_eng_char]['type'] == 'vowel':
                return self.eng_to_ban_map[eng_chars]['replace']
            else:
                return self.eng_to_ban_map[eng_chars]['short_form']
        else:
            return self.eng_to_ban_map[eng_chars]['replace']