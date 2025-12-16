from django.urls import path
from .views import category_list, document_list

app_name = 'documents'

urlpatterns = [
    path('', category_list, name='categories'),
    path('<slug:slug>/', document_list, name='category'),
]
