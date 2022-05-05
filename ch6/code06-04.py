#키보드로 입력한 값까지 합계 구하기
# hap = 0
# num = int(input("숫자를입력하세요"))
#
# for i in range(1,num+1,1):
#     hap += i
# print("1부터 %d까지의 합:%d"% (num,hap))

#시작값, 증가값, 끝값을 모두 입력받자
# hap = 0
# num1,num2,num3 = map(int,input("시작값 증가값 끝값을 입력하세요 :").split())
# for i in range(num1,num3+1,num2):
#     hap += i
# print(hap)

#사용자가 입력한 숫자의 단에서 구구단을 출력하는 프로그램
num = int(input("숫자를 입력하세요"))

for i in range(1,10,1):
    print("%d x %d = %d" % (num,i,num*i))