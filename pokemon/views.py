from hashlib import new
from django.http import HttpResponse
import pokemon
# from numpy import logical_and, logical_not
from pkg_resources import get_supported_platform
#from requests import put

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User, Pokemon

from .serializers import UserSerializer, PokemonSerializer

# /users/login
# uSUARIO VÁLIDO
# {
#     "name": "teste",
#     "password": "12345"
# }

@api_view(['GET', 'POST'])
def login(request):

    data = request.data

    if(request.method == 'POST'):

        user_name_input = data['name']
        try:
            usuario_cadastrado = User.objects.get(name=user_name_input)
            return Response(status=200, data = {'logged_in': True, 'selectedFirtsPokemon': usuario_cadastrado.selectedFirtsPokemon})
        except:
            return Response(status=404)

    else:
        return Response(status=200, data = {'aviso': 'esperando post para verificação do usuario'})
        
    
# /users/register
@api_view(['POST'])
def register(request):
    new_name = request.data['name']
    new_password = request.data['password']
    new_selectedFirtsPokemon = request.data['selectedFirtsPokemon']

    new_User = User(name = new_name, password = new_password, selectedFirtsPokemon = new_selectedFirtsPokemon)
    new_User.save()

    return Response(status=200)

# /users/<id>/delete
@api_view(['GET','DELETE'])
def delete(request, name):

    usuario = User.objects.get(name = name)
    if(request.method == 'DELETE'):
        usuario.delete()
        return Response(status=204)
    
    serialized_users = UserSerializer(usuario)
    return Response(serialized_users.data)

# /users/
@api_view(['GET'])
def users(request):
    try:
        usuarios = User.objects.all()
    except User.DoesNotExist:
        raise Http404()

    serialized_users = UserSerializer(usuarios, many=True)
    return Response(serialized_users.data)

# lorran users/<name>
# /users/<name>
@api_view(['GET', 'POST'])
def user(request, name):
    try:
        usuario = User.objects.get(name = name)
    except User.DoesNotExist:
        raise Http404()
    if(request.method == 'POST'):

        # new_name = request.data['name']
        # new_password = request.data['password']
        new_selectedFirtsPokemon = request.data['selectedFirtsPokemon']
        usuario.selectedFirtsPokemon = new_selectedFirtsPokemon;
        usuario.save()

    serialized_user = UserSerializer(usuario)
    return Response(serialized_user.data)

#####


# para os pokemons

# /pokemons/
@api_view(['GET'])
def pokemons(request):
    try:
        pokemons = Pokemon.objects.all()
    except Pokemon.DoesNotExist:
        raise Http404()

    serialized_pokemons = PokemonSerializer(pokemons, many=True)
    return Response(serialized_pokemons.data)

# /pokemons/<name>/
@api_view(['GET'])
def getUserPokemons(request, name):
    try:
        usuario = User.objects.get(name = name)
        pokemons = Pokemon.objects.filter(idUser = usuario)
    except User.DoesNotExist:
        raise Http404()

    serialized_pokemons = PokemonSerializer(pokemons, many=True)
    return Response(serialized_pokemons.data)

# /game/
@api_view(['POST'])
def includePokemon(request):
    new_id = request.data['id']
    new_idUser = User.objects.get(name =  request.data['idUser'])
    new_name = request.data['name']
    new_type = request.data['type']
    new_move1 = request.data['move1']
    new_move2 = request.data['move2']
    new_move3 = request.data['move3']
    new_srcImg = request.data['srcImg']
    new_favorite = request.data['favorite']

    new_Pokemon = Pokemon(id = new_id, idUser = new_idUser, name = new_name, type = new_type, move1 = new_move1, move2 = new_move2, move3 = new_move3, srcImg = new_srcImg, favorite = new_favorite)
    new_Pokemon.save()

    return Response(status=200)



@api_view(['GET','POST','DELETE'])
def api_postanddelete_pokemon(request, id):
    
    try:
        pokemon = Pokemon.objects.get(id = id)
    except Pokemon.DoesNotExist:
        raise Http404()

    if (request.method == 'DELETE'):
        pokemon.delete()
        return Response(status=204)

    serialized_pokemons = PokemonSerializer(pokemon)
    return Response(serialized_pokemons.data)



def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")