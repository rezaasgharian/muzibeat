from django.urls import path
from .views import Login, Register, Logout_View
from .views import Login, Register , Logout_view

urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('logout/', Logout_View, name="logout"),
    path('logout/', Logout_view, name="Logout_view"),
]