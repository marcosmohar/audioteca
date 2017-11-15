from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Artist
from .serializers import ArtistModelSerializer
from .permissions import GroupPatatasPermissions


# Create your views here.

class ListArtist(APIView):

    def get(self, request):
        """ Returns serialized artist data"""
        artists = Artist.objects.all()
        serializer = ArtistModelSerializer(artists, many=True)
        # permission for group Patatas
        permission_classes = (IsAuthenticated, GroupPatatasPermissions)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Save data to DB or returns an error if data is not valid"""
        serializer = ArtistModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailArtist(APIView):

    def _get_artist(self,id):
        try:
            artist = Artist.objects.get(id=id)
            return artist
        except Artist.DoesNotExist:
            raise Http404

    def get(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistModelSerializer(artist)
        return Response(serializer.data, status=status.HTTP_200_OK)    

    def put(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistModelSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = self._get_artist(id)
        serializer = ArtistModelSerializer(artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self):
        artist = self._get_artist(id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)