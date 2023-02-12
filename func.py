#지역변수(Local Variable), 전역변수(Global Veriable)

#지역변수
# def jeju_potato():
#     potato = "고구마"
#     print(potato)

# jeju_potato()

#전역변수

# potato = "감자"

# def jeju_potato():
#     global potato
#     print(potato)
#     potato = "고구마"
#     print(potato)

# jeju_potato()

# def jeju_potato():
#     potato = "고구마"
#     print(potato)

# print(potato)
# jeju_potato()

# def add(num1 , num2 = 20, num3 = 30):
#     return num1 + num2 + num3

# print(add(num1 = 20, num3 = 2))

# a, b = 20, 40
# def add(num1 = a, num2 = b):
#     return num1 + num2 

# a, b = 5, 10

# print(add())

# def add(*args):
#     sum = 0 
#     for i in args:
#         sum += i
#     print(sum)
# add(10, 20, 30, 40)

# def add(*args):
#     return args

# print(add(10, 20, 30, 40))

#키워드 매개변수

#키워드 = 특정값 형태로 {"키워드":"특정값"}

# def star_player(**kwargs):
#     for i in kwargs:
#         print(i)

# star_player(축구 = "손흥민", 야구 = "박용택", 농구 = "허재")

# def star_player(**kwargs):
#     for i, j in kwargs.items():
#         if "서장훈" in kwargs.values():
#             print("저는 LG팬이라 서장훈을 좋아했어요")
#         else:
#             print("{}는 역시 {}지".format(i,j))

# star_player(농구 = "서장훈")

# 매개변수 사용 순서 일반 매개변수, 가변 매개변수, 기본 매개변수, 키워드 매개변수 순으로 사용(순서 바뀌면 오류 발생) 
# def func_a(name, *args, address = "한국", **kwargs):
#     print(name, args, address, kwargs)

# func_a("홍길동", "옛날", "사람", address = "한양", 직업 = "도둑")

# 최대, 최소값을 구하기

# def max_min_search(*number):
#     max_num = number[0]
#     min_num = number[0]
#     for num in number:
#         if num > max_num:
#             max_num = num
#         elif num < min_num:
#             min_num = num
        
#     return max_num, min_num
# print(max_min_search(15,30,4,60,7,80,32))

def max_min_search(*number):
    return max(number), min(number)
    
print(max_min_search(15,30,4,60,7,80,32))