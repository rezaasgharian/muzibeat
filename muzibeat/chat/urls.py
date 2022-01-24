from django.urls import path
from .views import *

app_name = 'Chat'

urlpatterns = [
    path('chat/', index, name='index'),
    path('<str:room_name>/', room, name='room'),
    path('edit_chat/<int:pk>/', edit_chat.as_view(), name='edit'),
]
