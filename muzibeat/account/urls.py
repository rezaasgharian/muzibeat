from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('logout/', Logout_view, name="logout"),
    path('profile/', Profiles, name="profile"),
    path('update/', User_Update, name="update"),
    path('change/', Change_Password, name="change"),
    path('create/', Post_users, name="postuser"),
    path('User_post/<int:user_id>', User_post, name="User_post"),
    path('Search_user/<str:username>', Search_user, name="Search_user"),
]
