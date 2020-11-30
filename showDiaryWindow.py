import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from Upload_diary import Upload


class ShowDiaryWindow(QMainWindow):
    def __init__(self,choice_window):
        super().__init__()
        self.choice_window=choice_window

        # 윈도우 설정
        self.setupUI()

    def setupUI(self):
        showTitle=QLabel("내가 쓴 일기", self)
        showTitle.resize(1200, 100)
        font1 = showTitle.font()
        font1.setPointSize(25)
        font1.setBold(True)
        showTitle.setFont(font1)
        showTitle.setAlignment(Qt.AlignCenter)

        btnShow=QPushButton("일기 보기", self)
        btnShow.setGeometry(400, 650, 80, 30)
        btnShow.clicked.connect(self.showDiary)

        goHome = QPushButton("", self)
        goHome.move(800, 600)
        goHome.resize(128, 128)
        goHome.setStyleSheet("background-image : url(image/home.png);")
        goHome.clicked.connect(self.exist)

        self.show_contents=QLabel(self)
        self.show_contents.setAlignment(Qt.AlignCenter)
        self.show_contents.resize(1200,600)

        layout = QVBoxLayout()
        layout.addWidget(showTitle)
        layout.addWidget(goHome)
        layout.addWidget(btnShow)
        layout.addWidget(self.show_contents)

        self.setLayout(layout)

        self.setGeometry(300, 100, 1200, 800)  # x, y, w, h
        self.setWindowIcon(QIcon('image/baby.png'))
        self.setWindowTitle('일기 보기')
        self.show()

    def showDiary(self):
        file=open('diary.txt', 'r', encoding='utf-8')
        data=file.read()
        file.close()
        self.show_contents.setText(data)

        # file=open('diary.txt', 'r', encoding='utf-8')
        # for f in range(file.__sizeof__()):
        #     line=f.readline()
        #     print(line)

    def exist(self):
        self.hide()
        ch = self.choice_window
        ch.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showWindow = ShowDiaryWindow()
    showWindow.show()
    sys.exit(app.exec_())
