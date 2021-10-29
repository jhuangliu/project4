# poems/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('poems/', views.PoemList.as_view(), name='poem_list'),
    path('poems/<int:pk>',
         views.PoemDetail.as_view(), name='poem_detail'),
    
]
