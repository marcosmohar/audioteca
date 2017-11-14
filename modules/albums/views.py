from django.shortcuts import get_object_or_404
from .models import Album
from .serializers import AlbumModelSerializer, AlbumTracksSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permissions import GroupPataratasPermissions


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
#    serializer_class = AlbumModelSerializer
    serializer_class = AlbumTracksSerializer
    permission_classes = (IsAuthenticated, GroupPataratasPermissions)

class DetailGenericAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer