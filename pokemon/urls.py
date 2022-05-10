from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/users/', views.api_getandpost_users, name='all_users'),
    path('api/pokemons/', views.api_getandpost_pokemons, name='all_pokemons'),
    path('api/users/<id>', views.api_postanddelete_user, name='postedelete'),
    path('api/pokemons/<id>', views.api_postanddelete_pokemon, name='postedeletepokemon')
]