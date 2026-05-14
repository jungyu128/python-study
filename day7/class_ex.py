# class_ex.py
# 부모 클래스
class Passbook:
    def __init__(self,owner,balance): # 생성자
        #생성자(객체 생성하면서 초기값을 저장)       
        self.owner=owner
        self.balance=balance
    def deposit(self,money): #입금 함수
        self.balance += money
        print(f"{money}원 입금 완료")  
        print(f"현재 잔액은 {self.balance}원 입니다")  

    # 예) 출금 5000, 잔액 3000 => 잔액부족
    def withdraw(self,money): #출금 함수
        if money  <= self.balance:
            self.balance -= money
            print(f"{money}원 출금 완료")  
            print(f"현재 잔액은 {self.balance}원 입니다") 
        else:
            print("잔액 부족")
    def showInfo(self):
        print("예금주: ",self.owner)
        print("현재 잔액: ",self.balance)
# 자식 클래스
class MinusPassbook(Passbook): #상속
    #withdraw() 자식이 재정의(오버라이딩)
    def withdraw(self,money): #출금 함수
# 마이너스 한도: 잔액이 부족하더라도 
# (잔액 - 출금액) 결과가 -1,000,000원 이상이면 출금이 가능
        if (self.balance-money) >= -1000000:
            self.balance -= money
            print(f"{money}원 출금 완료")  
            print(f"현재 잔액은 {self.balance}원 입니다") 
        else:
            print("마이너스 한도 잔액 부족")

# 실행
# 객체 생성 account1 + 생성자 호출(예금주:홍길동, 잔액:100000)
account1 = Passbook("홍길동",100000)
# 입금 함수 호출 50,000원 입금
account1.showInfo()
account1.deposit(50000)
# 출금함수 호출 120,000 출금
account1.withdraw(120000)
# 출금함수 호출 70,000 출금
account1.withdraw(70000) 
# 마이너스 통장 객체(account2)  생성
# =>김철수 이름의 마이너스 통장(잔액 100,000원) 객체를 생성
# 마이너스 통장에서 120,000원 출금을 시도하여 정상 출금 및 잔액이 음수가  되는지 확인.
# 추가로 900,000원을 더 출금하여 마이너스 한도가 정상 작동하는지 확인

account2 = MinusPassbook("김철수",100000)
account2.showInfo()
account2.withdraw(120000) # 자식클래스 호출
account2.withdraw(9000000) 