from django.urls import path
from . import views

app_name = 'teams'  # пространство имён приложения

urlpatterns = [
    path('', views.teams_view, name='teams'),  # основная вкладка сборные
]
