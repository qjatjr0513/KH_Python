# print(1)

# while True:
#     for i in range(10):
#         print(i)

# def division():
#     num1 = input("첫번째 정수를 입력해주세요 >")
#     if num1.isdigit():
#         num2 = input("두번째 정수를 입력해주세요 >")
#         if num2.isdigit() and num2 != "0":
#             return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
#         else:
#             print("0이아닌 숫자로된 정수를 입력하세요.")
#     else:
#         print("숫자로된 정수를 입력하세요.")

# division()

# def division():
#     try:
#         num1 = input("첫번째 정수를 입력해주세요 >")
#         num2 = input("두번째 정수를 입력해주세요 >")

#         return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
#     except:
#         print("0이 아닌 숫자로된 정수를 입력해주세요 !!")
# division()

# def division():
#     num1 = input("첫번째 정수를 입력해주세요 >")
#     num2 = input("두번째 정수를 입력해주세요 >")

#     return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")

# division()

#ValueError, ZeroDivisionError, KeyboardInterrupt

# def division():
#     try:
#         num1 = input("첫번째 정수를 입력해주세요 >")
#         num2 = input("두번째 정수를 입력해주세요 >")

#         return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
#     except ValueError:
#         print("숫자로 된 정수를 넣어주세요 !!")
#     except ZeroDivisionError:
#         print("제발 !! 0을 입력하지 마세요!!")
# division()

# def division():
#     try:
#         num1 = input("첫번째 정수를 입력해주세요 >")
#         num2 = input("두번째 정수를 입력해주세요 >")

#         return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
#     except BaseException as e:
#         print("오류가 발생했어요!!")
#     finally:
#         print("정상적으로 나누기 함수가 호출 되었습니다.!")
# division()
# help(ValueError)
# help(ZeroDivisionError)
# help(KeyboardInterrupt)

# def division():
#     try:
#         num1 = int(input("첫번째 정수를 입력해주세요 >"))
#         num2 = int(input("두번째 정수를 입력해주세요 >"))

#         # return print(f"{num1}을 {num2}로 나눈 값은 {int(num1)/int(num2)}입니다.")
#         result = num1 / num2
#     except BaseException as e:
#         print("오류가 발생했어요!!")
#     else:
#         print("정상적으로 나누기 함수가 호출 되었습니다.!")
#         return print("{}을 {}로 나눈 값은 {}입니다.".format(num1, num2, result))
        
# division()

#화장실이 너무 급한 남자
class Toilet:
    def __init__(self):
        self.using = False
    
    def in_use(self):
        if self.using ==False:
            print("화장실을 사용합니다!")
            self.using = True
        else:
            raise Exception("안에 사람이 있어요 !! 잠시만 기다려주세요 !!!")

    def not_in_use(self):
        self.using == False
        print("안에 사람이 없습니다!")

man = Toilet()

while True:
    use = input("화장실을 사용하시겠습니까?(y/n)")
    try:
        if use == "y":
            man.in_use()
        else:
            man.not_in_use()
    except Exception as e:
        print(e)