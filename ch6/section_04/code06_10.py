# 무한루프로 입력한 두숫자의 합계를 반복하여 계산하는 프로그램
sum = 0
while True:
    num1,num2 = map(int,input("두 수 입력:").split())
    sum = num1 + num2
    print(sum)