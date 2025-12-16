from django.shortcuts import render

from django.shortcuts import render
from news.models import News

def home(request):
    latest_news = News.objects.filter(published=True).order_by('-created_at')[:4]
    return render(request, 'core/home.html', {'latest_news': latest_news})

