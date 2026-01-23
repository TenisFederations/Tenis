# core/views.py
from django.shortcuts import render
from .models import Partner

def home(request):
    partners = Partner.objects.all()
    context = {
        'partners': partners,
    }
    return render(request, 'core/home.html', context)
