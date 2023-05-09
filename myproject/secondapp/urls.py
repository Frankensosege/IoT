from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam1, name='exam1'),
    path('exam2/', views.exam2, name='exam2'),
    path('exam3/', views.exam3, name='exam3'),
    path('exam4/', views.exam4, name='exam4'),
    path('exam5/', views.exam5, name='exam5'),
]
