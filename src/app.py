import sys
from PyQt5 import QtWidgets
from src.Window import Window


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

run()
