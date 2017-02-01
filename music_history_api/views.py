# from django.shortcuts import render

from music_history_api.models import *
from music_history_api.serializers import *
# from rest_framework import generics
# from rest_framework.reverse import reverse
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.decorators import detail_route
from rest_framework import viewsets
# from rest_framework import renderers 
# from rest_framework import permissions
from django.contrib.auth.models import User

class GenreViewSet(viewsets.ModelViewSet):
    """
    The Genre view provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Genre's url for the `update` and `destroy` actions.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    
class ArtistViewSet(viewsets.ModelViewSet):
    """
    The Artist view provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Artist's url for the `update` and `destroy` actions.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    
class AlbumViewSet(viewsets.ModelViewSet):
    """
    The Album view provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Album's url for the `update` and `destroy` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    
class SongViewSet(viewsets.ModelViewSet):
    """
    The Song view provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Song's url for the `update` and `destroy` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

