from .models import Track
from .serializers import TrackModelSerializer, TrackAlbumSerializer
from rest_framework import viewsets
# Create your views here.

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all().select_related('album')
    serializer_class = TrackAlbumSerializer
