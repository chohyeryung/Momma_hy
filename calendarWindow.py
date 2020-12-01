import sys

import pymysql as pymysql
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic.properties import QtGui

from Upload_diary import Upload

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='111111',
    db='mama',
    charset='utf8'
)
class CalendarWindow(QMainWindow):

    def __init__(self,choice_window):
        super().__init__()
        self.choice_window=choice_window
        # 윈도우 설정
        self.setGeometry(300, 100, 1200, 800)  # x, y, w, h
        self.setStyleSheet("background-image : url(image/cal_back.jpg);")
        self.setWindowIcon(QIcon('image/baby.png'))
        self.setWindowTitle('일기 쓰기')

        # CalendarWidget 위젯 화면에 표시
        self.cal = QCalendarWidget(self)
        self.cal.setGeometry(120, 50, 970, 300)
        self.cal.setGridVisible(True)
        self.cal.selectionChanged.connect(self.calendar_change)
        self.cal.setVerticalHeaderFormat(0)

        # min max 기간 설정
        #self.cal.setMinimumDate(QDate(2020, 8, 25))
        #self.cal.setMaximumDate(QDate(2020, 8, 27))

        # Calendar 에서 선택한 값 표시할 QLabel
        self.calendar_label = QLabel(self)
        self.calendar_label.setGeometry(120, 370, 970, 30)
        self.calendar_label.setStyleSheet('background-color:#D3D3D3')

        self.b = QPlainTextEdit(self)
        self.b.insertPlainText("일기를 작성해요주세용.\n")
        font1 = self.b.font()
        font1.setPointSize(20)
        font1.setBold(True)
        self.b.setFont(font1)
        self.b.setGeometry(120, 420, 970, 200)
        self.b.setStyleSheet("background-image : url(image/cal_input.jpg);")

        self.setupUI()

    def setupUI(self):
        btn1 = QPushButton("저장", self)
        btn2 = QPushButton("취소", self)
        btn1.setGeometry(450, 650, 80, 30)
        btn1.clicked.connect(self.GoUpload)
        btn1.clicked.connect(self.show_dialog)
        self.msg = QMessageBox()
        btn2.setGeometry(650, 650, 80, 30)
        btn2.clicked.connect(self.exist)

    # Calendar Open 함수
    @pyqtSlot()
    def calendar_change(self):
        cal_date = self.cal.selectedDate()
        strDate = cal_date.toString('yyyy년 ' + 'MM월 ' +'dd일')  # QDate 를 str
        self.calendar_label.setAlignment(Qt.AlignCenter)
        font1=self.calendar_label.font()
        font1.setPointSize(25)
        font1.setBold(True)
        self.calendar_label.setFont(font1)
        self.calendar_label.setText(strDate)

    # 달력에서 현재를 선택
    @pyqtSlot()
    def select_today(self):
        self.cal.currentPageChanged(self, 2022, 10)

    def GoUpload(self):
        self.contents=''
        self.date=self.calendar_label.text()
        for line in self.b.toPlainText():
            self.contents+=line
        cur=conn.cursor()
        sql="INSERT INTO calendar (caldate, contents) VALUES (%s, %s)"
        cur.execute(sql, (self.date, self.contents))
        conn.commit()


    def exist(self):
        self.hide()
        ch=self.choice_window
        ch.show()

    def show_dialog(self):
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('일기 쓰기')
        self.msg.setText('일기가 저장되었습니다.')
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval = self.msg.exec_()

        # # 반환값 판단
        # print('QMessageBox 리턴값 ', retval)
        if retval == QMessageBox.Ok:
            self.exist()
        elif retval == QMessageBox.Cancel:
            print('messagebox cancel : ', retval)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = CalendarWindow()
    mainWindow.show()
    sys.exit(app.exec_())
