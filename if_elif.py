# lunch = input("점심메뉴를 골라주세요(제육덮밥, 돈까스, 김밥) > ")
# if lunch == "제육덮밥":
#     print("제육덮밥을 먹는다.")
# elif lunch == "돈까스":
#     print("돈까스를 먹는다.")
# elif lunch == "김밥":
#     print("김밥을 먹는다.")
# else:
#     print("점심을 굶는다.")

# number = 85

# if number > 90:
#     print("90보다 큰 수 입니다.")
# elif number > 80:
#     print("90보다 작고 80보다 큰 수 입니다.")
# elif number > 50:
#     print("80보다 작고 50보다 큰 수 입니다.")
# else:
#     print("50보다 작은 수 입니다.")

# and, or
#if 문 여러조건을 동시에 판별
#3의 배수이면서 짝수인 수를 판별해주는 조건식
# number = int(input("정수를 입력해주세요 > "))

# if number %3 == 0 and number %2 ==0:
#     print("3의 배수이면서 짝수입니다.")
# elif number %3 != 0:
#     print("3의 배수가 아닙니다.")
# else:
#     print("짝수가 아닙니다.")

# if number %3 == 0 or number %2 ==0:
#     if number %3 == 0 and number %2 != 0:
#         print("3의 배수입니다.")
#     elif number %3 == 0 and number %2 == 0:
#         print("3의 배수이면서 짝수입니다.")
#     else:
#         print("짝수 입니다.")
# else:
#     print("짝수가 아닙니다.")

domain = input("웹 사이트 주소를 입력해주세요 > ")
nation = domain.split(".")

# kr = 한국, uk = 영국, com = 기업, org = 기관, 알 수 없음
#가장 뒤쪽의 요소를 [-1]

if nation[-1] == "kr":
    print("한국")
elif nation[-1] == "uk":
    print("영국")
elif nation[-1] == "com":
    print("기업")
elif nation[-1] == "org":
    print("기관")
else:
    print("알 수 없음")