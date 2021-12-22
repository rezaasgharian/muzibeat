from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.core.exceptions import ValidationError
from knox.views import LoginView as KnoxLoginView
from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
import os
from django.http import HttpResponse



# Create your views here.
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


@api_view(['POST'])
def Music(request):
    if request.method == 'POST':
        if not request.data['title'] or len(request.data['title']) < 3:
            raise ValueError("title must be valid")
        if not request.data['description'] or len(request.data['description']) < 3:
            raise ValueError("description must be valid")
        if not request.data['artist'] or len(request.data['artist']) < 3:
            raise ValueError("artist must be valid")

        # up_song = request.FILES['song']
        # print(up_song)
        music_list = Song.objects.create(user_id=request.user.user_id, title=request.data['title'], description=request.data['description'],artist=request.data['artist'])
        if music_list:
            return HttpResponse(request.data)
        else:
            return HttpResponse("error")



        # if request.Files.get('song', False):
        #     songs = request.FILES.getlist('song')
        #     count = len(songs)
        #     if count > 10:
        #         raise ValidationError('Maximum number of songs must be 10')
        #     for sng in range(int(count)):
        #         ext = os.path.splitext(str(songs[sng]))[1]
        #         valid_extensions = ['.mp3']
        #     if not ext.lower() in valid_extensions:
        #         raise ValidationError('Unsupported file.')
        #     for song in songs:
        #         sng = Song.objects.create(song=song)
        #     sng.save()


@api_view(['POST'])
def album(request):
    if request.method == "POST":
        if not request.data['title'] or len(request.data['title']) < 3:
            raise ValidationError('title must be valid')
        if not request.data['description'] or len(request.data['description']) < 3:
            raise ValidationError('description must be valid')
        if not request.data['artist'] or len(request.data['artist']) < 3:
            raise ValidationError('artist must be valid')
        album_list = Album.objects.create(title=request.data['title'],description=request.data['description'],artist=request.data['artist'])
        if album_list:
            return HttpResponse(request.data)
        else:
            return HttpResponse("error")

@api_view(['POST'])
def artist(request):
    if request.method == "POST":
        if not request.data['name'] or len(request.data['name']) < 3:
            raise ValidationError('name must be valid')
        artist_list = Artist.objects.create(user_id=request.user.user_id,name=request.data['name'])
        if artist_list:
            return HttpResponse(request.data)
        else:
            return HttpResponse("error")
