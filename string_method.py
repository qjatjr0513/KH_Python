text = "            www.GOOGLE.com          "

# # print(len(text)) #문자열의 길이를 반환

# # txt_capitalize = text.capitalize() #첫 글자를 대문자로 변결

# # print(txt_capitalize)
# txt_upper = text.upper() #문자열 전체를 대문자로 변경

# txt_lower = text.lower() #문자열 전체를 소문자로 변경
# print(txt_upper) 
# print(txt_lower) 

# count, find, index

# g_cnt = text.count('G') #찾는 문자의 갯수를 반환
# g_cnt = text.count('GO')
# g_cnt = text.count('X')


# g_find = text.find('G') # 찾는 문자의 인덱스를 반환
# g_find = text.rfind('G')
# g_idx = text.index('G') # 찾는 문자의 인덱스를 반환
# g_idx = text.rindex('G') # 

# print(g_find)
# print(g_idx)

# text_naver = text.replace("GOOGLE", "NAVER")  # 문자열 치환
# print(text_naver)

# print(text.split('.'))
# print(text.split('OO')) #문자열을 분리

print(text)
stp =text.strip()
print(stp)
