import json
import sys
from PyQt4 import QtGui


with open('draft_map.json') as letter_map_file:
    banglaToEnglish = json.load(letter_map_file)

englishToBangla = {value: key for key, value in banglaToEnglish.items()}

print(englishToBangla['k']+englishToBangla['e'])

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(50, 50, 500, 300)
window.setWindowTitle("Test Qt")

window.show()
sys.exit(app.exec_())
