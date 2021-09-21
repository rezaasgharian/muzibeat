from django.urls import path
from .views import Posts , detail

urlpatterns = [
    path('posts/', Posts ,name="home"),
    path('posts/<slug:slug>', detail, name='detail'),
]