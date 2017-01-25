import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Qt Main Window")
        self.setWindowIcon(QtGui.QIcon("pencil.png"))

        # add main menu
        extract_action = QtGui.QAction("&Quit", self)
        extract_action.setShortcut("Ctrl+Q")
        extract_action.setStatusTip("Leave this app")
        # extractAction.triggered.connect(self.close_application())

        # self.setStatusBar()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("&File")
        file_menu.addAction(extract_action)

        self.organize()
        self.show()

    def organize(self):
        btn = QtGui.QPushButton("Click to CLOSE", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(150, 100)
        self.show()

    def close_application(self):
        print("Application closed!")
        sys.exit()


def run():
    app = QtGui.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


run()
