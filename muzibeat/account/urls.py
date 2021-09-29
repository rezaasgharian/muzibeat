from django.urls import path
from .views import Login, Register, Logout_View

urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('logout/', Logout_View, name="logout"),
]