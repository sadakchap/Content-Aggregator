from django import template
from news.models import NewsBox
register = template.Library()


@register.inclusion_tag('news/news_list.html')
def zeenews_latest(count=5):
    news = NewsBox.objects.filter(src_name='Zee News')[:count]
    return {'news': news}

@register.inclusion_tag('news/news_list.html')
def indiatv_latest(count=5):
    news = NewsBox.objects.filter(src_name='IndiaTV')[:count]
    return {'news': news}

@register.inclusion_tag('news/news_list.html')
def hindu_latest(count=5):
    news = NewsBox.objects.filter(src_name='The Hindu')[:count]
    return {'news': news}