from django.urls import path
from .views import Login, Register , Logout_view

urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('logout/', Logout_view, name="Logout_view"),

]