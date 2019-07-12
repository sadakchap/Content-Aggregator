from django.shortcuts import render
from news.scripts.indiatv import indiaTvscrape
from news.scripts.thehindu import hindu
from news.scripts.zeenews import zeenews
from .models import NewsBox
import os
import shutil
from django.conf import settings
import requests
# Create your views here.

def home(request):
    scrape()
    hindu()
    zeenews()
    news = NewsBox.objects.all()
    return render(request, 'home.html', {'news': news})


def scrape():
    session = requests.Session()
    session.headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36'}
    news_list = indiaTvscrape()
    for obj in news_list:
        if NewsBox.objects.filter(news_link=obj['news_link']).exists():
            pass
        else:
            news = NewsBox()
            news.src_name = obj['src_nm']
            news.src_link = obj['src_link']
            news.title = obj['news_title']
            news.news_link = obj['news_link']
            # stackoverflow solution
            img_src = obj['news_img_src']

            media_root = settings.MEDIA_ROOT
            if not img_src.startswith(("data:image", "javascript")):
                local_filename = img_src.split('/')[-1].split("?")[0]
                r = session.get(img_src, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)

                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media_root)


            # end of stackoverflow
            news.img = local_filename
            news.save()


