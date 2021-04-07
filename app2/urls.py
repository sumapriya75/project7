from django.shortcuts import render
from django.urls import path 
from app2 import views
urlpatterns = [
    path('index2/',views.index2,name='index2'),
    path('sample2/', views.sample2,name='sample2'),
]
