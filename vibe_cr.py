import requests
from bs4 import BeautifulSoup

r = requests.get("https://music.naver.com/listen/top100.nhn?domain=DOMESTIC_V2")
bs = BeautifulSoup(r.text, "html.parser")

# 가수의 목록
# 노래의 목록

song_name = []
artist_name = []

song = bs.select("td.name > a >span,ellipsis")
artist = bs.select("td._artist > a > span.ellipsis")

for s in range(len(song)):
    song_name.append(song[s].text)
for s in range(len(song)):
    artist_name.append(artist[a].text)
for s in range(len(0, 50)):
    print(f"순위 {i+1}위 - 가수: {artist_name[i].strip()} - 곡명 : {song_name[i]}")
