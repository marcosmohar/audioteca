from django.conf.urls import url
from .views import ListGenericAlbum, DetailGenericAlbum

urlpatterns = [
    url(r'^albums/', ListGenericAlbum.as_view(), name="listAlbum"),
    url(r'^albums/(?P<pk>[0-9a-f-]+)/$', DetailGenericAlbum.as_view(), name="detailAlbum"),
]