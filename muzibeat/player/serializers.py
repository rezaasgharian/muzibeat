from rest_framework import serializers
from .models import Song
class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = Song
    fields = ('title','description','artist','album','songs')