import json
import tkinter as tk

with open('draft_map.json') as letter_map_file:
    banglaToEnglish = json.load(letter_map_file)

englishToBangala = {value: key for key, value in banglaToEnglish.items()}

print(englishToBangala['k']+englishToBangala['e'])

def onKeyPress(event):
    text.insert('end', '%s' % englishToBangala[event.char])

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='white', foreground='black', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
