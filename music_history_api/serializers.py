from rest_framework import serializers
from music_history_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User



class GenreSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Genre
    """

    class Meta:
        model = Genre
        fields = ('url', 'name',)
        # depth = 2


class ArtistSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Artist
    """

    class Meta:
        model = Artist
        fields = ('url', 'name', 'year_formed',)


class AlbumSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Album
    """

    class Meta:
        model = Album
        fields = ('url', 'title', 'genre', 'artist',)
        depth = 1


class SongSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Song
    """

    class Meta:
        model = Song
        fields = ('url', 'title', 'duration', 'genre', 'artist', 'album',)
        depth = 1
