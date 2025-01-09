import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,QMessageBox, QPlainTextEdit) # QMessageBox: 메시지박스 위젯

from PyQt5.QtGui import QIcon #아이콘을 추가하기 위한 라이브러리
class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.te1 = QPlainTextEdit() #텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)


        self.btn1 = QPushButton('Message',self) #버튼 추가
        self.btn1.clicked.connect(self.activateMessage) #버튼 클릭시 핸들러 함수 연결


        vbox = QVBoxLayout() #수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1) # 수직 레이아웃에 텍스트 에디트 추가
        # vbox.addStretch(1) #빈공간
        vbox.addWidget(self.btn1) #버튼 위치
        vbox.addStretch(1) #빈공간

        self.setLayout(vbox) #빈 공간 - 버튼 - 빈공간 순으로 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png')) #윈도 아이콘 추가
        self.resize(256,256)
        self.show()
    
    def activateMessage(self): #버튼을 클릭할 때 동작하는 함수 : 메시지 박스 출력
        #핸들러함수 수정 : 메시지가 텍스트 에디트에 출력되도록
        # QMessageBox.information(self,"information","Button clicked!")
        self.te1.appendPlainText("Button clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())