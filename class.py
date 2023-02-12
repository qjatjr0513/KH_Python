# class BreadMold:
#     #속성 == 변수
#     category = "크림빵"


# bread = BreadMold()
# bread.price = 3000
# bread_choco = BreadMold()
# bread_choco.category = "초코크림빵"
# #참조연산자 .format()
# print("{}의 가격은 {}입니다.".format(bread.category, bread.price))
# print(bread_choco.category, bread_choco.price)

# class BreadMold:
#     #속성 == 변수
#     category = "크림빵"
#     def make_bread(self):
#         print("빵을 만들어 냅니다.")

# bread = BreadMold()
# bread.make_bread()

# int(), str(), float(), bool(), tuple() .....type()
#클래스

# number = 1
# # 1 데이터 int 인스턴스(객체)
# a = 1.0

# print(isinstance(number, int))
# print(isinstance(a, float))
# # id() = 객체의 주소값을 반환
# print(id(number))
# print(id(a))
# print(id(1))

# text = "a"
# numbers = (1,2,3,4,5,6)

# print(type(number))
# print(type(text))
# print(type(numbers))

# text1 = 12345
# text2 = "12345"

# print(id(text1), id(text2))
# print(id(text2), id(int(text2)))


# class BreadMold:
#     category = "빵"

# bread1 = BreadMold()
# bread2 = BreadMold()
# bread3 = BreadMold()

# bread1.price = 3000
# bread2.category = "붕어빵"
# bread3.category = "잉어빵"

# print(bread1.category, bread2.category, bread3.category)

# #dir() 이름공간에 있는 모든 속성을 리스트로 반환

# print(dir(bread1))
# print(dir(bread2))
# print(dir(BreadMold))
# print(dir(str))


#__init__ 생성자 매서드
#__del__ 소멸자 매서드
# class BreadMold:
#     category = "빵"

#     def __init__(self, category, price):
#         self.category = category
#         self.price = price
#         print("빵을 만들었습니다.")
    
#     def __str__(self):
#         return "{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price)
#     def __del__(self):
#         print("빵이 없어졌습니다.")

# bread1 = BreadMold("붕어빵", 3000)
# bread1 = BreadMold("빵", 1000)
# bread2 = BreadMold("잉어빵", 4000)
# # print("{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price))
# # print("{}의 가격은 {}원 입니다.".format(bread2.category, bread2.price))
# print(bread1)

#super, 부모
#sub, 자식

class ParentRestaurant:
    price = 15000

    def __init__(self, name, menu, recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe

    def __str__(self):
        return "가게 이름: {}, 가게의 메뉴 : {}, 메뉴의 조리법: {}".format(self.name, self.menu, self.recipe)

    def __del__(self):
        pass

class ChildRestaurant(ParentRestaurant):
    price = 20000
    # marketing = "온라인 마케팅"

    def __init__(self, name, menu, recipe, marketing):
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing = marketing

    def __str__(self):
        return super().__str__() + ", 마케팅 방법: {}".format(self.marketing)
# restaurant_info = ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다.")
# restaurant_info2 = ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다.")
# print(restaurant_info2.marketing)

restaurnt_info = ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다.", "온라인")
print(restaurnt_info)

print(issubclass(ChildRestaurant, ParentRestaurant))
print(issubclass(ParentRestaurant, ChildRestaurant))
print(issubclass(int , ChildRestaurant))