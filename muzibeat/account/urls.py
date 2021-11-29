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
    path('edit/<int:pk>/', edit_post.as_view(), name='edit_post'),
    path('post_details/<int:post_id>/', Post_details, name='post_details'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('Search_user/<str:username>', Search_user, name="Search_user"),
    path('like', like, name="like_post"),
    path('report', report, name="report"),
    path('follow', follow, name="follow"),
    path('comment', comment, name="comment"),
    path('category_user/<str:title>', Category_user, name="category_user"),
]
