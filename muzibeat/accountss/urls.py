from django.urls import path
from .views import *

app_name = 'accountss'
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
    path('block', block, name="block"),
    path('category_user/<str:title>', Category_user, name="category_user"),
    path('followings_posts/<int:self_id>', followings_posts, name="followings_posts"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accountss/password_reset_form.html',email_template_name='accountss/password_reset_email.html',subject_template_name='accountss/password_reset_subject.txt',success_url = reverse_lazy('accountss:password_reset_done')), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'accountss/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accountss/password_reset_complete.html'), name="password_reset_complete"),


    # path(
    #     'reset_password/',
    #     auth_views.PasswordResetView.as_view(email_template_name = 'accountss/password_reset_email.html'),
    #     name='reset_password'
    # ),
    # path(
    #     'reset_password_sent/',
    #     auth_views.PasswordResetDoneView.as_view(),
    #     name='password_reset_done'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('password_reset_complete')),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset_password_complete/',
    #     auth_views.PasswordResetCompleteView.as_view(),
    #     name='password_reset_complete'
    # )
]
