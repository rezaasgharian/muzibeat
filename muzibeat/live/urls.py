from django.urls import path, include
from .views import *

app_name = 'live'
urlpatterns = [
    path('webcam_feed/', Home, name='Home'),
    path('stream/', stream, name='stream'),

]
