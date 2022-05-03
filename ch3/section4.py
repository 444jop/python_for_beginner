# 파이썬의 2진수를 10진수로
print(0b10010011)
print(int('10010011',2))

# 파이썬의 16진수를 10진수로
print(0x93)
print(int('93',16))

#10진수를 2진수로


#진수변환 프로그램
sel = int(input("몇진수를 원하세요?"))
if sel != 16 and sel != 8 and sel!= 2 and sel!= 10:
    exit("16,10,8,2중 하나만 입력하세요")
num = input("값 : ")

if sel == 16:
    num = int(num,16)
if sel == 8:
    num = int(num, 8)
if sel == 10:
    num = int(num, 10)
if sel == 2:
    num = int(num, 2)
print(hex(num))
print(num)
print(oct(num))
print(bin(num))