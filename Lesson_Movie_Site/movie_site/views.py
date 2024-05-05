from rest_framework import viewsets, permissions
from .models import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .serializers import *



class WomenAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class UserProfileViewSets(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = WomenAPIListPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSets(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = WomenAPIListPagination

    #filter


class ActorViewSets(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = WomenAPIListPagination


class DirectorViewSets(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = WomenAPIListPagination
    #filter


class GenreViewSets(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = WomenAPIListPagination
    #filter


class MovieViewSets(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = WomenAPIListPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'genres', 'directors', 'year']
    search_fields = ['title']


class MovieShotsViewSets(viewsets.ModelViewSet):
    queryset = MovieShots.objects.all()
    serializer_class = MovieShotsSerializer
    pagination_class = WomenAPIListPagination


class RatingViewSets(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = WomenAPIListPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewViewSets(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = WomenAPIListPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
