from django.shortcuts import render
from news.scripts.zeenews import zeenews
from news.scripts.indiatv import indiaTvscrape
from news.scripts.thehindu import hindu
from news.scripts.news18 import news18
from news.scripts.timesofindia import timesofindia
from news.scripts.indiatoday import indiatoday
# Create your views here.

def home(request):
    scrape()
    return render(request, 'home.html', {})


def scrape():
    zeenews()
    indiaTvscrape()
    hindu()
    news18()
    timesofindia()
    indiatoday()