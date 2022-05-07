#구구단이 거꾸로 출력되게 해보자
for i in range(9,0,-1):
    line = ""
    for k in range(9,1,-1):
        line = line + str("%2d X%2d =%2d ##"%(k,i,i*k))
    print(line)