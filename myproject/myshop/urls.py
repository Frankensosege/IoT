from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.index, name='myshop'),
    path('my_actor/', views.my_actor, name='my_actor'),
    path('my_dbconn/', views.my_dbconn, name='my_dbconn'),
]
