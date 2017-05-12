import sys
from PyQt4 import QtGui
from src.Window import Window


def run():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

run()
