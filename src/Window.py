import sys
from PyQt4 import QtGui, QtCore
from src.Eng2BanMap import Eng2BanMap


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Qt Main Window")
        self.setWindowIcon(QtGui.QIcon("pencil.png"))

        self.text_editor = QtGui.QTextEdit()

        # menu action
        action_quit = QtGui.QAction("&Quit", self)
        action_quit.setShortcut("Ctrl+Q")
        action_quit.triggered.connect(self.close_application)

        action_editor = QtGui.QAction("&Open Editor", self)
        action_editor.setShortcut("Ctrl+E")
        action_editor.triggered.connect(self.open_editor)

        # status bar
        self.statusBar().showMessage("Home screen")

        # menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(action_quit)
        file_menu.addAction(action_editor)

        self.organize_home()
        self.show()

    def organize_home(self):
        # btn = QtGui.QPushButton("Click to CLOSE", self)
        # btn.clicked.connect(self.close_application)
        # btn.resize(btn.sizeHint())
        # btn.move(150, 200)

        # close action
        close_action = QtGui.QAction(QtGui.QIcon("pencil.png"), 'Quit with icon', self)
        close_action.triggered.connect(self.open_editor)

        # toolbar
        toolbar = self.addToolBar("A Toolbar")
        toolbar.addAction(close_action)

        self.show()

    def open_editor(self):
        self.setCentralWidget(self.text_editor)
        self.text_editor.setFocus()
        self.text_editor.keyPressEvent = self.editor_key_press_event

    def editor_key_press_event(self, key_event):
        modifiers = QtGui.QApplication.keyboardModifiers()

        if modifiers & QtCore.Qt.ShiftModifier:
            english_char = chr(key_event.key())
        else:
            english_char = chr(key_event.key() + 32)

        english_to_bengali = Eng2BanMap()
        bengali_char = english_to_bengali.get_bengali_character(english_char)
        print(english_char + " --> " + bengali_char)
        self.text_editor.insertPlainText(bengali_char)
        last_bengali_char = self.text_editor.toPlainText()[-1]

    @staticmethod
    def close_application():
        print("Application closed!")
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

run()

