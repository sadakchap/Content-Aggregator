from bs4 import BeautifulSoup
import requests

url = 'https://www.indiatvnews.com/'
source = requests.get(url).text

soup = BeautifulSoup(source, "lxml")

news_box=soup.find('ul', class_=['normal'])

requests.packages.urllib3.disable_warnings()

def indiaTvscrape():
    news_list = []
    for news_story in news_box.find_all('li')[:7]:
        news_link = news_story.find('a')
        news_img_src = news_link.find('img').get('data-original')
        news_card = news_story.find('div',class_='text_box')
        news_title = news_card.find('h2', class_='title').a.text

        # print(news_link.get('href'))
        # print(news_img_src)
        # print(news_title.strip())
        # print('*'*80)

        news_list.append({
            'src_nm':'IndiaTV',
            'src_link':url, 
            'news_title': news_title, 
            'news_img_src': news_img_src,
            'news_link': news_link.get('href')
        })
    return news_list




# news_story = soup.find('ul', class_=['normal']).li

# print(news_story)
