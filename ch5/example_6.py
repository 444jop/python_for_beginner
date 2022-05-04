#다음 중첩 if 문을 elif를 사용하는 코드로 변경하시오
# score = int(input("점수를 입력하세요"))
# if score >= 60:
#     print("합격입니다")
# else:
#     if  score >= 40:
#         print("불합격이지만 과락은 아닙니다.")
#     else:
#         print("불합격이면서 과락입니다.")

score = int(input("점수를 입력하세요"))
if score >= 60:
    print("합격입니다.")
elif score >= 40:
    print("불합격이지만 과락은 아닙니다.")
else:
    print("불합격이면서 과락입니다.")