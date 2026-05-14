# exception__ex.py

fruits = ["사과", "바나나", "오렌지"]

try:
    index = int(input("번호 입력 (0~2): "))
    # 과일을 선택하는 코드도 try 안에 있어야 IndexError를 잡을 수 있습니다.
    print(f"선택한 과일: {fruits[index]}")

except IndexError:
    print("인덱스 범위를 벗어났습니다. 0에서 2 사이의 숫자를 입력하세요.")
except ValueError:
    print("유효한 숫자를 입력하세요. 문자는 입력할 수 없습니다.")