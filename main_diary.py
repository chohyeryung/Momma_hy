from PyQt5.QtGui import QIcon

from calendarWindow import CalendarWindow
from choice import Choice
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Main_Diary(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        text_edit = QPlainTextEdit()
        text = open('diary.txt', 'r', encoding='utf-8').read()
        text_edit.setPlainText(text)

        # with open('diary.txt') as data:
        #     lines = data.readlins()

    def initUI(self):
        self.setWindowTitle('Momma')
        self.setWindowIcon(QIcon('image/baby.png'))
        self.setGeometry(300, 100, 1200, 800)

        # label1 = QLabel()
        # label1.setAlignment(Qt.AlignCenter)






if __name__=="__main__":
    app=QApplication(sys.argv)
    main=Main_Diary()
    main.show()
    sys.exit(app.exec_())