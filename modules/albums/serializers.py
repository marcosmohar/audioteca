from rest_framework import serializers
from .models import Album
from modules.tracks.serializers import TrackModelSerializer

class AlbumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        # puedes seleccionar por fields o por exclude, no ambos
        fields = ('__all__')
        #fields = ('id', 'name', 'biography', 'photo', 'albums', 'is_band')
        #exclude = ('primary_genre',)

class AlbumTracksSerializer(serializers.ModelSerializer):
    tracks = TrackModelSerializer(many=True, read_only=True)
    class Meta:
        model = Album
        fields = ('id', 'name', 'cover', 'track_count', 'genre','tracks')