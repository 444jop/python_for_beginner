#구구단을 표형식으로 출력하는 프로그램
for i in range(1,10):
    line = ""
    for k in range(2,10):
        line = line + str("%2d X%2d =%2d ##"%(k,i,i*k))
    print(line)