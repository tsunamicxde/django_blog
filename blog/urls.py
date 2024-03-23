from django.urls import path
from . import views
from .views import article_detail

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('add/', views.add_article, name='add_article'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
]
