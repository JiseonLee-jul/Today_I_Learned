import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_movie_reviews(mcode, page_num = 10): # mcode : movie 코드

  movie_review_df = pd.DataFrame(columns=("Title", "Score", "Review"))

  #url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=203101&target=after"
  url = "https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=" \
    + str(mcode) + "&target=after"

  idx = 0

  for _ in range(0, page_num):
    movie = requests.get(url)
    movie_soup = BeautifulSoup(movie.content, 'lxml')

    review_list = movie_soup.find_all('td', {'class': 'title'})
    for review in review_list:
      title = review.find('a', {'class': 'movie color_b'}).get_text()
      score = review.find('em').get_text()
      
      #review_text = review.find('br').get_text()
      #review_text = review.find('a', {'class': 'report'}).get('onclick')
      review_text = review.find('a', {'class': 'report'}).get('onclick').split(',')[2]
      movie_review_df.loc[idx] = [title, score, review_text]
      idx += 1
      print("#", end = "")


  return movie_review_df
