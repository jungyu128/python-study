# fun3.py
def dis_price(price, discount):
    return price * (1 - discount / 100)
//할입금액 10000원, 할인율 10% -> 10000 * (1 - 10 / 100) = 9000원 작성
# 테스트
print(dis_price(10000, 10))  # 9000.0
print(dis_price(50000, 20))  # 40000.0
print(dis_price(100000, 30))  # 70000.0
print(dis_price(200000, 50))  # 100000.0

#만원에서 할인율 10퍼센트된 1000원으로 코드 작성해줘
print(dis_price(10000, 10))  # 9000.0


#키워드 인수는 인수의 인수의 이름을 명시적으로 지정해서 값을 매개변수로 저장하는 방법으로 작성해줘
print(dis_price(price=10000, discount=10))  # 9000.0
#키워드 인수는 인수의 순서와 상관없이 값을 매개변수로 저장할 수 있어
print(dis_price(discount=10, price=10000))  # 9000.0
sub(100,200,300) # 100, 200, 300이 순서대로 a, b, c에 저장
sub(y=20,x=10,z=30) # 10, 20, 30이 순서와 상관없이 x, y, z에 저장
sub(z=55,y=35,x=15) # 15, 35, 55가 순서와 상관없이 x, y, z에 저장
    

