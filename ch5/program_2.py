# 연산자
select = int(input("1. 입력한 수식 계산 \n2. 두 수 사이의 합계"))

if select == 1:
    numstr = input("수식을 입력하세요\n")
    answer = eval(numstr)
    print("결과는 :%s" % answer)
elif select == 2:
    num1,num2 = map(int,input("두 수를 입력하세요").split())
    answer = 0
    for i in range(num1,num2+1):
        answer = answer + i
    print("결과는 :%d"% answer)
else:
    print("1 또는 2를 입력해야합니다")