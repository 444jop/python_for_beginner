# 중첩 for 문을 이용하여 구구단을 2단 부터 9 단까지 출력해보자

for i in range(2,10,1):
    print("## %d단 ##" % i)
    for k in range(1,10,1):
        print('%d x %d = %d' % (i,k,i*k))
    print("")