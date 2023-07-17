from django.shortcuts import render
from .models import Artiles


def news_home(reguest):
    news = Artiles.objects.all()
    return render(reguest, 'news/news_home.html', {'news': news})
