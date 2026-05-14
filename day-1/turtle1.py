import turtle #모듈

t=turtle.Turtle() # turtle 객체 생성, t 변수에 할당
t.shape("turtle") # 모양 설정

radius = 50 # 반지름 설정
t.circle(radius) # 반지름이 50인 원을 그린다
t.fd(30) # 앞으로 이동
t.circle(radius)
t.fd(30) # 앞으로 이동
t.circle(radius)
t.fd(50)
for _ in range(4): #반복문 
    t.forward(2*radius)
    t.right(90) # 오른쪽 이동
# 한 변의 길이가 반지름*2인 정사각형 그리기
for _ in range(3): #반복문 
    t.forward(2*radius) 
    t.left(120) # 오른쪽 이동
# 한 변의 길이가 반지름*2인 정삼각형 그리기