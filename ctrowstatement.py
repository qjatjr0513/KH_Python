# text = input("성을 입력해주세요 >")
# text2 = input("이름을 입력해주세요 >")
# print(text +text2)

# number = input("첫 번째 정수를 입력해주세요 >")
# number2 = input("두 번째 정수를 입력해주세요 >")
# print(int(number) + int(number2))

# number = float(input("첫 번째 정수를 입력해주세요 >"))
# number2 = float(input("두 번째 정수를 입력해주세요 >"))
# print(number + number2)

# weather = "비"

# if weather == "비":
#     print("우산을 챙겨주세요")

# study_time = int(input("오늘의 공부시간을 입력해주세요 >"))

#만약에 오늘 공부할시간이 3시간 이상이라면 파이썬 공부
# if study_time >= 3:
#     print("오늘은 파이썬 공부를 합시다 !")

# #만약에 오늘 공부할 시간이 3시간 미만이라면 오늘은 놀자
# if study_time < 3:
#     print("오늘은 시간이 별로 없으니까 놀자 !")

#만약에 오늘 공부할 시간이 3시간 이상이고
#여섯시간 이하라면 파이썬 공부
# if 6 >= study_time >= 3 :
#     print("오늘은 파이썬 공부를 합시다 !")

# odd = int(input("정수를 입력해주세요 >"))

# 홀수, 짝수
# 1,3,5,7,9 / 2 == %1
# 2,4,5,8,0

# if odd[-1] == "1" or odd[-1] == "3" or odd[-1] == "5" or odd[-1] == "7" or odd[-1] == "9":
#     print("입력하신 정수는 홀수 입니다.")

# if odd % 2 == 1:
#     print("입력하신 정수는 홀수 입니다.")
# else:
#     print("입력하신 정수는 짝수 입니다.")

#13자리의 숫자중에서 7번째 숫자
#123456-1234567
number = input("주민번호를 입력해주세요 >")
odd = int(number[7])

if odd % 2 == 0: # 짝수라면
    print("여성입니다.")
else: # 짝수가 아니라면 == 홀수라면
    print("남성입니다.")