from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='get_users'),
    path('users/<name>/delete', views.delete, name='delete'),
    path('users/register', views.register, name='create'),
    path('users/login', views.login, name='login'), 

    path('pokemons/', views.pokemons, name='get_pokemons'),
    path('game/', views.includePokemon, name='catchPokemon'),

    
]