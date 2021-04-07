from django.shortcuts import render
from django.urls import path 
from app1 import views
app_name="app1"
urlpatterns = [
    path('index1/',views.index1,name='index1'),
    path('sample1/', views.sample1,name='sample1'),
    path("sample1_app1/",views.sample1,name="sample1"),
    path("<data>/",views.carry_data,name="carry_data"),
    path("fact/<num>/",views.facto,name="facto"),
    path("add/<num1>/<num2>/",views.add,name="add"),
]
