import sys
from PyQt4 import QtGui


class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Qt Main Window")
        self.setWindowIcon(QtGui.QIcon("pencil.png"))
        self.show()

app = QtGui.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())