# 오른쪽 중간 인기급상승 웹툰
# 정적 웹페이지 데이터 가져오기
# 태그 찾기 편리한 모듈, 서버 접속을 위한 라이브러리, 데이터프레임을 만들기 위한 라이브러리
from bs4 import BeautifulSoup
import requests
import pandas as pd

res_comic = requests.get('https://comic.naver.com/index')
soup_comic = BeautifulSoup(res_comic.text, 'lxml')

# ol : ordered list
comic_all = soup_comic.find("ol", attrs = {"id":"realTimeRankFavorite"}).find_all("li")

list_comic_all = []
for rank, comic in enumerate(comic_all):
  list_comic = []
  list_comic.append(rank + 1)
  list_comic.append(comic.a.text.strip())
  list_comic.append('https://comic.naver.com' + comic.a['href'])
  list_comic_all.append(list_comic)
  
df_comic = pd.DataFrame(list_comic_all, columns = ['순위', '제목', '링크'])

df_comic
