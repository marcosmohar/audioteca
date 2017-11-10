from rest_framework import serializers
from .models import Album

class AlbumModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        # puedes seleccionar por fields o por exclude, no ambos
        fields = ('__all__')
        #fields = ('id', 'name', 'biography', 'photo', 'albums', 'is_band')
        #exclude = ('primary_genre',)