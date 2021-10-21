from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', Posts ,name="home"),
    path('posts/<slug:slug>', detail, name='detail'),
    path('adcreate/', Post_admin, name="admin_create_post"),
]