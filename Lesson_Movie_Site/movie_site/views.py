from rest_framework import viewsets
from models import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class WomenAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class ProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    pagination_class = WomenAPIListPagination


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    pagination_class = WomenAPIListPagination
    #filter

class ActorViewSets(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    pagination_class = WomenAPIListPagination


class DirectorViewSets(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    pagination_class = WomenAPIListPagination
    #filter


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    pagination_class = WomenAPIListPagination
    #filter


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    pagination_class = WomenAPIListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'genres', 'directors', 'year']
    search_fields = ['title']

class MovieShotsViewSets(viewsets.ModelViewSet):
    queryset = MovieShots.objects.all()
    pagination_class = WomenAPIListPagination


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    pagination_class = WomenAPIListPagination


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    pagination_class = WomenAPIListPagination