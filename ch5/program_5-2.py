#program_2.py처럼 두 수를 입력 받고 두 숫자 사이의 합계를 구하는 프로그램 제작
#증가하는 수는 1이 아닌 입력받아 증가 시킨다.

num1 , num2 = map(int,input("두 수를 입력하세요.").split())
add = int(input("더할 숫자를 입력하세요."))
total = 0
for i in range(num1,num2+1,add):
    total = total + i
print("합은 : %d 입니다." % total)
