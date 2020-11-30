import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from game_hmama import Game_hmama
from game_mama import Game_mama
from game_mmama import Game_mmama

class ChooseLevel(QMainWindow):
    def __init__(self,choice_window):
        super().__init__()
        self.choice_window=choice_window
        # 윈도우 설정
        self.setcslUi()

    def setcslUi(self):
        HighLevel = QPushButton('상', self)
        MiddleLevel = QPushButton('중', self)
        LowLevel = QPushButton('하', self)
        print('hi')

        LowLevel.move(800,300)
        LowLevel.resize(200,200)
        font1 = LowLevel.font()
        font1.setPointSize(30)
        font1.setBold(True)
        LowLevel.setFont(font1)
        LowLevel.setStyleSheet("Color : red")
        LowLevel.clicked.connect(self.GoLowGame)


        MiddleLevel.move(500, 300)
        MiddleLevel.resize(200, 200)
        font1 = MiddleLevel.font()
        font1.setPointSize(60)
        font1.setBold(True)
        MiddleLevel.setFont(font1)
        MiddleLevel.setStyleSheet("Color : red")
        MiddleLevel.clicked.connect(self.GoMdGame)


        HighLevel.move(200, 300)
        HighLevel.resize(200, 200)
        font1 = HighLevel.font()
        font1.setPointSize(120)
        font1.setBold(True)
        HighLevel.setFont(font1)
        HighLevel.setStyleSheet("Color : red")
        HighLevel.clicked.connect(self.GoHighGame)

        layout = QVBoxLayout()
        layout.addWidget(LowLevel)
        layout.addWidget(MiddleLevel)
        layout.addWidget(HighLevel)

        self.setLayout(layout)
        self.setWindowTitle('난이도 고르기')
        self.setWindowIcon(QIcon('image/baby.png'))
        self.setGeometry(300, 100, 1200, 800)
        self.setStyleSheet("background-image : url(image/black.jpg);")
        self.show()

    def GoLowGame(self):
        self.lgame = Game_mama()

    def GoMdGame(self):
        self.mgame = Game_mmama()

    def GoHighGame(self):
        self.hgame = Game_hmama()

    def exist(self):
        self.hide()
        ch = self.choice_window
        ch.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cslevel = ChooseLevel()
    cslevel.show()
    sys.exit(app.exec_())
