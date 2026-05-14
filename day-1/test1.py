ap = input("상품 이름을 입력하세요 : ")
qu = int(input("상품 수량을 입력하세요 : "))
price = int(input("가격을 입력하세요 : "))
total = price *qu
print(f"{ap}의 총 가격은 {qu*price}원입니다.")
# print 안에서 f는 f-string이라 하며 포멧 문자열
#  ==>f" {변수 값}  ""
print(ap+"의 총 금액은 ",total,"원입니다.")

print(ap+"의 총 금액은 "+str(total)+"원입니다.")
# 숫자->문자로 변환 : str
# 실수는 float만 있음(8바이트)