from dataclasses import field
from rest_framework import serializers
from .models import Pokemon, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','password']

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'idUser', 'name', 'type', 'move1', 'move2', 'move3','srcImg', 'favorite']