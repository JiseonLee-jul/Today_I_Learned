# 네이버 검색 API 활용 - 웹검색
# 추가 다른 활용 방법은 아래 가이드 참
# https://developers.naver.com/docs/serviceapi/search/blog/blog.md#%EB%B8%94%EB%A1%9C%EA%B7%B8


# 1. 먼저 item 구성 살펴보기
import os
import sys
import urllib.request
# https://developers.naver.com/apps/#/myapps/p6tNlETVaE7YU3htQVJq/overview
client_id = "YOUR_CLIENT_ID" # ID 입력
client_secret = "YOUR_CLIENT_SECRET" # PASSWORD 입력
encText = urllib.parse.quote("WORD") # 검색할 단어 입력
url = "https://openapi.naver.com/v1/search/webkr?query=" + encText # web 검색 : json 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200): # rescode == 200일 경우만 정상 출력
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)



# 2. 데이터프레임으로 변환
import os
import sys
import urllib.request

import pandas as pd
import json
import re # 정규식

client_id = "YOUR_CLIENT_ID" # ID 입력
client_secret = "YOUR_CLIENT_SECRET" # PASSWORD 입력
query = urllib.parse.quote("WORD") # 검색할 단어 입력

idx = 0
display = 100 
start = 1
end = 1000
sort = 'sim'

web_df = pd.DataFrame(columns = ('Title', 'Link', 'Description')) # DataFrame 생성

for start_index in range(start, end, display) :

  url = "https://openapi.naver.com/v1/search/webkr?query=" + query \
  + "&display=" + str(display) \
  + "&start=" + str(start_index) \
  + "&sort" + sort

  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",client_id)
  request.add_header("X-Naver-Client-Secret",client_secret)
  response = urllib.request.urlopen(request)
  rescode = response.getcode()
  
  if(rescode==200):
      response_body = response.read()
      
      response_dict = json.loads(response_body.decode('utf-8')) # json
      items = response_dict['items']

      for item_index in range(0, len(items)):
        remove_tag = re.compile('<.*?>') # Tag 제거하기
        title = re.sub(remove_tag, '', items[item_index]['title'])
        link = items[item_index]['link']
        description = re.sub(remove_tag, '', items[item_index]['description'])
        web_df.loc[idx] = [title, link, description]
        idx += 1

  else:
      print("Error Code:" + rescode)

web_df
