import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class RecipeWindow(QMainWindow):
    def __init__(self,choose_window):
        super().__init__()
        self.choose_window=choose_window
        # 윈도우 설정
        self.setcslUi()

    def setcslUi(self):
        goHome = QPushButton('', self)

        goHome.move(450, 600)
        goHome.resize(68, 68)
        goHome.setStyleSheet("background-image : url(image/pepper.png);")
        goHome.clicked.connect(self.exist)

        layout = QVBoxLayout()

        self.setLayout(layout)
        self.setWindowTitle('게임 설명서')
        self.setWindowIcon(QIcon('image/manual.png'))
        self.setGeometry(500, 200, 950, 700)
        self.setStyleSheet("background-image : url(image/recipe.jpg);")
        self.show()

    def exist(self):
        self.hide()
        ch = self.choose_window
        ch.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rcwindow = RecipeWindow()
    rcwindow.show()
    sys.exit(app.exec_())
