# #list [] 안에 ,
# list_a = [1, 2, 3, 4]
# list_b = ["a", "b","c"]
# list_c = [True, False]
# list_d = [1, "a", True]

# print(list_a)
# print(list_b)
# print(list_c)
# print(list_d)

# numbers = [0,1,2,3,4,5,6,7]

# print(numbers[0])
# print(numbers[3:5])
# print(numbers[1:])
# print(numbers[-3:-1])
# list_lang = ["JAVA", "C", "Python", "Go"]
# print(list_lang[2][2:4])

# list_lang[1] = "C++"

# print(list_lang)

# list_lang[1:3] = ["C#", "Python3"]

# print(list_lang)

# print(len(list_lang))

#append() 리스트 맨 뒤에 제일 마지막 인덱스(-1)
# list_lang.append("Ruby")
# print(list_lang)

# list_a = [1,2,3]
# list_lang.append(list_a)
# print(list_lang[-1])


# # list_lang.extend([4,5,6])
# list_lang.extend("JavaScript")
# print(list_lang)

# # insert(index, data)
# list_lang.insert(0, "R")
# print(list_lang)

# pop(), remove()

# print(list_lang.pop(0))
# print(list_lang)

# list_lang.remove("Python")
# print(list_lang)

# del list_lang[1]
# print(list_lang)

#숫자, 알파벳, 한글

#numbers = [1000, 5000, 160, 100, 20, 3450]

# numbers.sort(reverse = True) #오름차순으로 정렬
# print(numbers)

# numbers.reverse() #리스트 안의 요소를 역순으로 변경
# print(numbers)

# names = ["banana", "apple", "carrot"]  

# names.sort()
# print(names)

# list_lang = ["JAVA", "C", "Python", "Go"]
# numbers = [1, 200, 3, 50, 5, 66, 7, 55, 9]

# # in 연산자와 not in 연산자

# print(50 in numbers)
# print("C" in list_lang)
# print("Java script" in list_lang)

# print(50 not in numbers)
# print("C" not in list_lang)
# print("Java script" not in list_lang)

# text = ["가", "나", "다"]

# print(text[0])
# print(text[1])
# print(text[2])

# print(text[-1])
# print(text[-2])
# print(text[-3])

# print(text[1:2])

td_number = [[10, 20, 30],[1, 2, 3]]

print(td_number[1][2])
print(td_number[0][0:2])
print(td_number[1][1:3])