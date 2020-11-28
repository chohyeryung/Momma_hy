import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from calendar import Calendar

from calendarWindow import CalendarWindow
from game_mama import Game_mama
from showDiaryWindow import ShowDiaryWindow

class Choice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.choiceUI()

    def choiceUI(self):
        btnDiary=QPushButton('', self)
        btnGame=QPushButton('',self)
        btnShowDiary=QPushButton('',self)

        btnDiary.move(100,250)
        btnDiary.resize(300,300)
        btnDiary.setStyleSheet("background-image : url(image/giveme_diary.jpg);")
        btnDiary.clicked.connect(self.GoDiary)

        btnGame.move(450, 250)
        btnGame.resize(300, 300)
        btnGame.setStyleSheet("background-image : url(image/mamma.jpg);")
        btnGame.clicked.connect(self.GoGame)

        btnShowDiary.move(800, 250)
        btnShowDiary.resize(300, 300)
        btnShowDiary.setStyleSheet("background-image : url(image/show_diary.jpg);")
        btnShowDiary.clicked.connect(self.ShowDiary)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(btnDiary)
        vbox.addWidget(btnGame)
        vbox.addStretch(1)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setWindowTitle('Momma')
        self.setWindowIcon(QIcon('image/baby.png'))
        self.setGeometry(300,100,1200,800)
        self.show()

    def GoDiary(self):
        self.calw = CalendarWindow(self)
        self.calw.show()
        self.hide()

    def ShowDiary(self):
        self.choicesh = ShowDiaryWindow(self)
        self.choicesh.show()
        self.hide()

    def GoGame(self):
        self.gamew = Game_mama()
        self.gamew.show()
        self.hide

if __name__=="__main__":
    app=QApplication(sys.argv)
    choice=Choice()
    choice.show()
    sys.exit(app.exec_())