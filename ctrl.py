# ch 6.6.2 ctrl.py

class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
    
    def calculate(self): # calculate 메서드 추가. 내용은 나중에 만들기
        num1 = float(self.view.le1.text()) # 첫번째 라인 에디트에 입력된 숫자를 읽어옴
        num2 = float(self.view.le2.text()) # 두번째 라인 에디트에 입력된 숫자를 읽어옴
        operator = self.view.cb.currentText() # 콤보박스에 선택된 연산자 확인

        if operator == '+': #연산자가 '+'면 결과를 스트링으로 리턴
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        else:
            return "Calculation Error"
        
    
    def connectSignals(self): #btn1을 클릭하면 calculate결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda:self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)
    
    def sum(self, a, b): # 덧셈 함수 추가
        return str(a+b)
    def sub(self, a, b): # 뺄셈 함수 추가
        return a - b
    def mul(self, a, b): # 곱셈 함수 추가
        return a*b
    def div(self, a, b): # exception 처리를 쓰도록 고침
        try:
            if(b == 0):
                return Exception("Divisor Error")
           
        except Exception as e:
            return e
        
        return a/b
    def pow(self, a, b): # 제곱연산 함수 추가
        return pow(a, b)
    
    