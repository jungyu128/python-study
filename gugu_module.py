def v_gugudan():
    for i in range(2, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")
        print()  # 단이 끝날 때마다 줄바꿈
def h_gugudan():
    for i in range(1, 10):
        for j in range(2, 10):
            print(f"{j} x {i} = {j * i}", end="\t")  # 탭으로 구분하여 출력
        print()  # 줄바꿈