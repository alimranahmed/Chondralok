import json

with open('draft_map.json') as letter_map_file:
    banglaToEnglish = json.load(letter_map_file)

englishToBangala = {value: key for key, value in banglaToEnglish.items()}

print(englishToBangala['k']+englishToBangala['e'])