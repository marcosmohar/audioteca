from .models import Track
from .serializers import TrackModelSerializer, TrackAlbumSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all().select_related('album')
    serializer_class = TrackModelSerializer
    # para proteger vistas 
    permission_classes = (IsAuthenticated,)
