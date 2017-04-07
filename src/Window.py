import sys

from PyQt4 import QtGui, QtCore

from src.core.Engine import Eng2BanMap


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.english_to_bengali = Eng2BanMap()
        self.last_bengali_char = ' '

        self.setGeometry(50, 50, 700, 400)
        self.setWindowTitle("Chondralok")
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
        self.statusBar().showMessage("Write in Bangla...")

        # menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(action_quit)
        file_menu.addAction(action_editor)

        self.organize_home()
        self.show()

    def organize_home(self):
        # close action
        open_editor = QtGui.QAction(QtGui.QIcon("pencil.png"), 'Open editor', self)
        open_editor.triggered.connect(self.open_editor)

        # toolbar
        toolbar = self.addToolBar("A Toolbar")
        toolbar.addAction(open_editor)

        self.show()

    def open_editor(self):
        self.setCentralWidget(self.text_editor)
        self.text_editor.setFocus()
        self.text_editor.keyPressEvent = self.editor_key_press_event

    def editor_key_press_event(self, key_event):
        try:
            modifiers = QtGui.QApplication.keyboardModifiers()
            bengali_char = chr(key_event.key())  # Value Error occur here

            if ord('A') <= key_event.key() <= ord('Z'):
                if modifiers & QtCore.Qt.ShiftModifier:
                    english_char = chr(key_event.key())
                    bengali_char = self.english_to_bengali.get_bengali_character(english_char, self.last_bengali_char)
                else:
                    english_char = chr(key_event.key() + 32)
                    bengali_char = self.english_to_bengali.get_bengali_character(english_char, self.last_bengali_char)
            self.text_editor.insertPlainText(bengali_char)
            self.last_bengali_char = self.text_editor.toPlainText()[-1]
        except ValueError:
            print("ERROR: A key pressed that cannot be converted to ASCI code")
            return

    @staticmethod
    def close_application():
        print("Application closed")
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

run()

