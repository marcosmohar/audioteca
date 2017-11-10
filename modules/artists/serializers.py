from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    biography = serializers.CharField(max_length=500)

class ArtistModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        # puedes seleccionar por fields o por exclude, no ambos
        fields = ('__all__')
        #fields = ('id', 'name', 'biography', 'photo', 'albums', 'is_band')
        #exclude = ('primary_genre',)