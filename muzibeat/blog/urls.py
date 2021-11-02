from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('like/', views.image_like, name="like"),
]