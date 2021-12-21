from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('apii/',hello_world , name='chat')
]