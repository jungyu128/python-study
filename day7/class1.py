# class1.py
# 클래스

class Board:
    def set_data(self, title, author):
        self.title = title #self는 this와 같은 의미로, 객체 자신을 가리킴
        self.author = author
b1 = Board()
b1.set_data("파이썬", "홍길동")
print(b1.title)
print(b1.author)
