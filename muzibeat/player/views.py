from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from django.core.exceptions import ValidationError
from django.core import serializers
from knox.views import LoginView as KnoxLoginView
from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from django.contrib.auth.decorators import login_required
import os
from django.http import HttpResponse, JsonResponse



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
        artist_list = get_object_or_404(Artist,user=request.user.user_id)
        music_list = Song.objects.create(user_id=request.user.user_id, title=request.data['title'], description=request.data['description'],artist=artist_list, songs=request.FILES['song'])
        if music_list:
            return HttpResponse(request.data)
        else:
            return HttpResponse("error")



class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        # if not request.data['artist'] or len(request.data['artist']) < 3:
        #     raise ValidationError('artist must be valid')
        artist_list = get_object_or_404(Artist, user_id=request.user.user_id)
        print(artist_list)
        album_list = Album.objects.create(title=request.data['title'],description=request.data['description'],artist=artist_list)
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



@login_required(login_url='/login/')
@api_view(['POST'])
def apisongLike(request):
    if request.method == "POST":
        song_id = request.data['id']
        if SongLike.objects.filter(user_id=request.user.user_id,song_id=song_id).exists():
            SongLike.objects.filter(user_id=request.user.user_id,song_id=song_id).delete()
            return HttpResponse("disliked")
        else:
            newlike = SongLike(user_id=request.user.user_id, song_id=song_id)
            newlike.save()
            return HttpResponse('liked')



@login_required(login_url='/login/')
@api_view(['POST'])
def apisongreport(request):
    if request.method == "POST":
        song_id = request.data['id']
        message = request.data['message']
        if Songreport.objects.filter(user_id=request.user.user_id, song_id=song_id).exists():
            return HttpResponse("This song is reported before")
        else:
            reports = Songreport(user_id=request.user.user_id, message=message, song_id=song_id)
            reports.save()
            return HttpResponse("Thanks for informing us... we will check it")



@login_required(login_url='/login/')
@api_view(['POST'])
def apiplaylist(request):
    if request.method == "POST":
        song_id = request.data['id']
        if PlayList.objects.filter(user_id=request.user.user_id, song_id=song_id).exists():
            return HttpResponse("This song is already in playlist")
        else:
            playlist = PlayList(user_id=request.user.user_id, song_id=song_id)
            playlist.save()
            return HttpResponse("This song is added to your playlist")



@login_required(login_url='/login/')
@api_view(['GET'])
def apisonglist(request):
    data=list(Song.objects.values())
    # serilized_objects =serializers.serialize('json',[songlist,])
    return JsonResponse(data,safe=False)


@api_view(['POST'])
def apiartistmusics(request):
    if request.method == 'POST':
        artist_id = request.data['id']
        print(artist_id)
        artistsongs = serializers.serialize("json",Song.objects.filter(artist_id=artist_id))
        return Response(artistsongs)



@api_view(['POST'])
def apialbummusics(request):
    if request.method == 'POST':
        album_id = request.data['id']
        albumsongs = serializers.serialize("json",Song.objects.filter(album_id=album_id))
        return Response(albumsongs)

