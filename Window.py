import sys
from PyQt4 import QtGui, QtCore
import Eng2BanMap


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Qt Main Window")
        self.setWindowIcon(QtGui.QIcon("pencil.png"))

        # menu action
        action_quit = QtGui.QAction("&Quit", self)
        action_quit.setShortcut("Ctrl+Q")
        action_quit.triggered.connect(self.close_application)

        # status bar
        self.statusBar().showMessage("Home screen")

        # menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(action_quit)

        self.organizeHome()
        self.show()

    def organizeHome(self):
        btn = QtGui.QPushButton("Click to CLOSE", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(150, 200)

        # close action
        close_action = QtGui.QAction(QtGui.QIcon("pencil.png"), 'Quit with icon', self)
        close_action.triggered.connect(self.close_application)

        # toolbar
        toolbar = self.addToolBar("A Toolbar")
        toolbar.addAction(close_action)

        self.show()

    def close_application(self):
        print("Application closed!")
        sys.exit()

    def keyPressEvent(self, QKeyEvent):
        english_to_bengali = Eng2BanMap.Eng2BanMap()
        bengali_char = english_to_bengali.get_bengali_character(chr(QKeyEvent.key() + 32))
        print(chr(QKeyEvent.key() + 32))
        print(bengali_char)


def run():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


run()
