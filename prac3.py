import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select(' #body-content > div> div > table.list-wrap > tbody > tr ')

# movies (tr들) 의 반복문을 돌리기
rank = 1

for song in songs:
    # movie 안에 a 가 있으면,
    a_tag = song.select_one('td.info > a')
    if a_tag is not None:
        title = song.select_one('.title').text
        title2= title.strip()
        star = song.select_one('.artist').text
        print(rank,title2,star)
        rank += 1