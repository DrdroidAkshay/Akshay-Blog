from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('review', views.review, name="review"),
    path('blog', views.blog, name="blog"),
    path('blogpost/<str:slug>', views.blogpost, name="blog"),
]