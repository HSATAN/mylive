# _*_ coding:utf-8 _*_
from django.contrib import admin
from django.urls import path, include
from blog import views
urlpatterns = [
    path('login', views.blog_login, name = 'blog_login'),
    path('register', views.register, name = 'register'),
    path('is_login', views.is_login, name='is_login'),
    path('add', views.add_article, name= 'add_article')
]