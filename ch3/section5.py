#제곱
a = 100 ** 100
print(a)

a = 0xFF
b = 0o77
c = 0b1111

print(a,b,c)

a= 3.14
b=3.14e5
print(type(a))
print(type(b))

a,b = 9,2
print(a//b)

num = hex(input())
if 0 < num < 10 or ('A' <= num <= 'F'):
    print(int(num,16))
else:
    print("16진수가 아닙니다.")