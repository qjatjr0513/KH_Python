# # requests
# #BeautifulSoup
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://www.naver.com")
# bs = BeautifulSoup(r.content, "html.parser")

# # h3 = bs.select("h3 > a")
# # selecter = bs.select("div#u_skip")
# selecter = bs.find("div", {"class":"partner_box"})
# # print(h3[0].text)
# # print(h3[0].name)
# # print(h3[0].attrs)
# # print(h3)
# print(selecter.text)

import requests
from bs4 import BeautifulSoup

r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8")
bs = BeautifulSoup(r.content, "html.parser")

weather = bs.select_one("dl.summary_list > dd.desc")

print("오늘의 체감온도는 : {}도 입니다.".format(weather.text))