#두 사람이 주사위를 던져 더 큰 수가 나오면 이기는 게임이다.
#A가 이기거나 B가 이기거나 비기는 결과가 나와야 한다.
import random
a = random.randint(1,6)
b = random.randint(1,6)

if a > b:
    print("A가 이겼습니다. %d %d" % (a,b))
elif b > a:
    print("B가 이겼습니다.%d %d" % (a,b))
else:
    print("비겼습니다.%d %d" % (a,b))