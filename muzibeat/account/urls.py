from django.urls import path
from .views import *


app_name = 'account'
urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('/logout/', Logout_view, name="logout"),
    path('profile/', Profiles, name="profile"),
    path('update/', User_Update, name="update"),
]
