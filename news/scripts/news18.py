from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.news18.com/').text

soup = BeautifulSoup(source, "lxml")

news_box = soup.find('ul', class_='lead-mstory')

for news_story in news_box.find_all('li')[:7]:
    news_link = news_story.find('a')
    news_img_src = None
    news_title = news_link.text
    print(news_link.get('href'))
    print(news_img_src)
    print(news_title.strip())
    print('*'*80)


