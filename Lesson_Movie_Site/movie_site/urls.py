from django.urls import path, include
from .views import *

urlpatterns = [

    path('accounts/', include('allauth.urls')),

    path('profiles/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='profile_list'),
    path('profiles/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='profile_detail'),


    path('categories/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('categories/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),


    path('actor/', ActorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='actor_list'),
    path('actor/<int:pk>/', ActorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='actor_detail'),


    path('director/', DirectorViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='director_list'),
    path('director/<int:pk>/', DirectorViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='director'),


    path('genre/', GenreViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='genre_list'),
    path('genre/<int:pk>/', GenreViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='genre_detail'),


    path('movie/', MovieViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='movie_list'),
    path('movie/<int:pk>/', MovieViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='movie_detail'),


    path('movie_shots/', MovieShotsViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='movie_shots_list'),
    path('movie_shots/<int:pk>/', MovieShotsViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='movie_shots_detail'),

    path('rating/', RatingViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='rating_list'),
    path('rating/<int:pk>/', RatingViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),


    path('reviews/', ReviewViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='review_list'),
    path('reviews/<int:pk>/', ReviewViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='review_detail'),
]
