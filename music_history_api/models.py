from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model): 
    """
    Class to create a table representing a Genre

    Extension of models.Model

    Variables:
        name: the name of the genre
       
    Author: Sam Phillips
    """

    name = models.CharField(max_length=100, default='')
    
    def __str__(self):
        """
        Method to create a string representing the genre

        Returns the genre's name
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Genre table of the music_history_api
        """
        ordering = ('name',)


class Artist(models.Model): 
    """
    Class to create a table representing an Artist

    Extension of models.Model

    Variables:
        name: the name of the artist
        year_formed: the year the artist/band was created
       
    Author: Sam Phillips
    """

    name = models.CharField(max_length=100, default='')
    year_formed = models.DateTimeField()
    
    def __str__(self):
        """
        Method to create a string representing the artist

        Returns the artist's name
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Genre table of the music_history_api
        """
        ordering = ('name',)


class Album(models.Model): 
    """
    Class to create a table representing an Album, which shares a relationship to the Artist of that album and its Genre.

    Extension of models.Model

    Variables:
        title: the name of the album
        genre: the foreign key of the album's genre
        artist: the foreign key of the artist which created the album
    Author: Sam Phillips
    """

    title = models.CharField(max_length=100, default='')
    genre = models.ForeignKey(Genre, related_name="albums", on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing the album

        Returns the album's title
        """
        return self.title

    class Meta:
        """
        Class defining metadata for results of querying the Album table of the music_history_api
        """
        ordering = ('title',)


class Song(models.Model): 
    """
    Class to create a table representing a Song, which shares a relationship to the Artist of that song, its Genre, and its Album.

    Extension of models.Model

    Variables:
        title: the name of the song
        duration: the length of the song in seconds
        genre: the foreign key of the song's genre
        artist: the foreign key of the artist which created the song
        album: the foreign key of the album the song was published on
    Author: Sam Phillips
    """

    title = models.CharField(max_length=100, default='')
    duration = models.IntegerField()
    genre = models.ForeignKey(Genre, related_name="songs", on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE)
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing the song

        Returns the song's title
        """
        return self.title

    class Meta:
        """
        Class defining metadata for results of querying the Song table of the music_history_api
        """
        ordering = ('title',)