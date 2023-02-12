# list [] tuple ()

# numbers = (1, 2, 3, 4)
# numbers = 1,2,3,4
# print(numbers)

# numbers = (1, )
#print(numbers)

# 튜플은 추가나 삭제가 불가능 (append(), extend(), insert() 사용불가)
# numbers = (1,2,3,(4,5, (6,7))) 
# numbers = (1,2,3)
# numbers = 1, 2, 3, 4
# print(numbers + numbers)
# print(2 * numbers)
# print(numbers)
# print(numbers.index(3))
# print(numbers[2])

# number1 = numbers[0]
# number2 = numbers[1]
# number3 = numbers[2]

# number1, number2, *number3 = numbers

# print(number1, number2, number3)
# print(numbers)
# print(id(numbers))
# numbers += 5, 6,
# print(numbers)
# print(id(numbers))

#Add 123, 문자, True, ("튜플")은 추가 가능
#[1,2,3], {keys: values}

# week = {"월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "월요일"}
# week.add("화요일")
# # week.add([1,2,3])
# print(week)

# a = {0, "abc", False}
# a.add(1)
# print(a)

# week = {"월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "월요일"}
# week.add(("일주일",))
# print(week)
# week.update(("일주일",))
# print(week)
# week.update(["일주일"], {"한달" :123})
# print(week)

# week = set(["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일", "금요일"])
# print(week)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

#합집합
print(a | b)
#교집합
print(a & b)
#차칩합
print(a - b)
print(b - a)

a.remove(4)
print(a)