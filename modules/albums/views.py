from django.shortcuts import get_object_or_404

from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Album
from .serializers import AlbumModelSerializer, AlbumTracksSerializer
from .permissions import GroupPataratasPermissions


class ListGenericAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumTracksSerializer
    #permission_classes = (IsAuthenticated, GroupPataratasPermissions)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    filter_fields = ('country', 'currency', 'price')
    search_fields = ('name', 'genre')

class DetailGenericAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumModelSerializer