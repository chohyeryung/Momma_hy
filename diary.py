import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Diary(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn=QPushButton('Quit',self)
        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Momma')
        self.setWindowIcon(QIcon('image/baby.png'))
        self.setGeometry(300, 100, 1200, 800)
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Diary()
    sys.exit(app.exec_())