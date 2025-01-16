# ch 5.2.1 ctrl.py

class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def calculate(self): # calculate 메서드 추가. 내용은 나중에 만들기
        pass
    
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)
    
    def sum(self, a, b): # 덧셈 함수 추가
        try:
            return str(a+b)
        except:
            return "Calculation Error"
    