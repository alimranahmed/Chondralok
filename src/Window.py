import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from src.core.Engine import Engine


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.engine = Engine()
        self.last_eng_chars = [' ', ' ', ' ']

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
        modifier = QtGui.QApplication.keyboardModifiers()
        shift_modifier = QtCore.Qt.ShiftModifier

        try:
            if ord('A') <= key_event.key() <= ord('Z'):
                pressed_eng_char = Window.get_eng_char(key_event, modifier, shift_modifier)
            elif key_event.key() == Qt.Key_Backspace:
                self.text_editor.textCursor().deletePreviousChar()
                return
            elif key_event.key() == Qt.Key_Return:
                self.text_editor.insertPlainText("\n")
                return
            else:
                pressed_eng_char = chr(key_event.key())

        except ValueError as e:
            print("Key cannot be converted to character")
            return

        replace_map = self.engine.get_ban_char(pressed_eng_char, self.last_eng_chars)

        self.last_eng_chars[0] = self.last_eng_chars[1]
        self.last_eng_chars[1] = pressed_eng_char
        if replace_map['replace_count'] == 0:
            self.text_editor.insertPlainText(replace_map['ban_char'])
        elif replace_map['replace_count'] == 1:
            self.text_editor.textCursor().deletePreviousChar()
            self.text_editor.insertPlainText(replace_map['ban_char'])
        elif replace_map['replace_count'] == 2:
            self.text_editor.textCursor().deletePreviousChar()
            self.text_editor.textCursor().deletePreviousChar()
            self.text_editor.insertPlainText(replace_map['ban_char'])

    @staticmethod
    def get_eng_char(key_event, modifier, shift_modifier):
        key = key_event.key()
        return chr(key) if modifier and shift_modifier else chr(key + 32)

    @staticmethod
    def close_application():
        print("Application closed")
        sys.exit()
