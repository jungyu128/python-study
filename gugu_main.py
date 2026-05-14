def v_gugudan():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()

def h_gugudan():
    for i in range(1, 10):
        for j in range(2, 10):
            print(f"{j} x {i} = {j * i}", end="\t")
        print()

while True:
    choice = input("세로형 구구단은 1, 가로형 구구단은 2, 종료는 0을 입력하세요: ")
    
    if choice == '1':
        print("세로로 출력되는 구구단:")
        v_gugudan()
    elif choice == '2':
        print("가로로 출력되는 구구단:")
        h_gugudan()
    elif choice == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")