from django.db import models
from django.contrib.auth.models import User
from datetime import date


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=255)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=16)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='directors/')

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.IntegerField(default=2024)
    country = models.CharField(max_length=100)
    directors = models.ManyToManyField(Director, related_name='film_director')
    actors = models.ManyToManyField(Actor, related_name='film_actor')
    genres = models.ManyToManyField(Genre, related_name='genres')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField(default=0)
    fees_in_usa = models.PositiveIntegerField(default=0)
    fess_in_world = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class MovieShots(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, related_name='movie_shots', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Rating(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Review(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField(max_length=2000)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"
