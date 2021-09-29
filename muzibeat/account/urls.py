from django.urls import path
from .views import Login, Register

urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
]