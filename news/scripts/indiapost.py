from bs4 import BeautifulSoup
import requests

url = 'https://www.indiapost.com/'
source = requests.get(url).text

soup = BeautifulSoup(source, "lxml")

news_box = soup.find('ul', class_=['article-array', 'content-category'])
print(news_box)