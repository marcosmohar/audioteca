from rest_framework import serializers
from .models import Track
#from modules.albums.serializers import AlbumModelSerializer

class TrackSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    duration = serializers.CharField(max_length=500)

class TrackModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        # puedes seleccionar por fields o por exclude, no ambos
        fields = ('__all__')
        #fields = ('id', 'name', 'biography', 'photo', 'albums', 'is_band')
        #exclude = ('primary_genre',)

class TrackAlbumSerializer(serializers.ModelSerializer):

    # llamas el AlbumModelSerializer y lo pasas como parametro a fields
    # regresa la info del album en lugar de el id
    # album = AlbumModelSerializer(read_only=True)
    class Meta:
        model = Track
        fields = ('id', 'name', 'duration', 'url_youtube', 'album')