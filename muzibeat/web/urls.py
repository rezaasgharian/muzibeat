from django.urls import path
from .views import *

app_name = 'web'
urlpatterns = [
    path('contact/', contact, name="web"),
    path('about/', about, name="about"),

]
