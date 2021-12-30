from knox import views as knox_views
from django.urls import path, include
from .views import *

app_name = 'player'
urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/createMusic/', Music, name="createMusic"),
    path('api/createAlbum/', album, name="createAlbum"),
    path('api/createArtist/', artist, name="createArtist"),
    path('api/songUpload/', FileView.as_view(), name="fileUpload"),
    path('api/songlike/', apisongLike, name="songlike"),
    path('api/songreport/', apisongreport, name="songreport"),
    path('api/playlist/', apiplaylist, name="playlist"),
    path('api/songlist/', apisonglist, name="songlist"),
]