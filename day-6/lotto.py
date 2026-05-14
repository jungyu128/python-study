
import random   
def lotto():
    numbers = random.sample(range(1, 46), 6) #1~45까지의 숫자 중에서 6개를 랜덤으로 뽑는다.
    numbers.sort() #뽑은 숫자를 오름차순으로 정렬한다.
    return numbers
# 테스트
print(f"로또번호는 {lotto()}")  # 예시 출력: [3, 12, 25, 33, 41, 44]
