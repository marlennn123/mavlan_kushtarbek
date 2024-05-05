from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'age', 'description', 'image']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Movie
        fields = ['title', 'tagline', 'description', 'poster', 'year', 'country', 'directors', 'actors', 'genres', 'world_premiere', 'budget', 'fees_in_usa', 'fess_in_world', 'category']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        directors_data = instance.directors.all()
        representation['directors'] = [{
            'id': director.id,
            'name': director.name,
            'age': director.age,
            'description': director.description,
            'image': director.image.url if director.image else None,
        } for director in directors_data]
        return representation

    def get_genres(self, obj):
        return {
            'id': obj.genres.id,
            'name': obj.genres.name,
        }

class MovieShotsSerializer(serializers.ModelSerializer):
    # movie = MovieSerializer()
    class Meta:
        model = MovieShots
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    # user = UserProfileSerializer()
    # movies = MovieSerializer()
    class Meta:
        model = Rating
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


