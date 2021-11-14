from django.urls import path
from .views import *
app_name = 'administrator'
urlpatterns = [
    path('posts/', Posts ,name="home"),
    path('posts/<slug:slug>', detail, name='detail'),
    path('category/<slug:slug>',categry,name="category"),
]