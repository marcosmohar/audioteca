from django.shortcuts import get_object_or_404
from .models import Album
from .serializers import AlbumModelSerializer
from rest_framework import generics
# Create your views here.

class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer

class DetailGenericAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer