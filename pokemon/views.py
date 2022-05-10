from hashlib import new
from django.http import HttpResponse
import pokemon

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Pokemon, User

from .serializers import UserSerializer, PokemonSerializer

@api_view(['GET', 'POST'])
def api_getandpost_users(request):
    try:
        usuarios = User.objects.all()
    except User.DoesNotExist:
        raise Http404()

    if(request.method == 'POST'):

        new_name = request.data['name']
        new_password = request.data['password']

        new_User = User(name = new_name, password = new_password)
        new_User.save()
        
    serialized_users = UserSerializer(usuarios, many=True)
    return Response(serialized_users.data)

# para os pokemons

@api_view(['GET', 'POST'])
def api_getandpost_pokemons(request):
    try:
        pokemons = Pokemon.objects.all()
    except Pokemon.DoesNotExist:
        raise Http404()

    if(request.method == 'POST'):
        new_id = request.data['id']
        new_idUser = User.objects.get(name =  request.data['idUser'])
        print("######################")
        print(new_idUser)
        print("######################")
        new_name = request.data['name']
        new_type = request.data['type']
        new_move1 = request.data['move1']
        new_move2 = request.data['move2']
        new_move3 = request.data['move3']
        new_srcImg = request.data['srcImg']
        new_favorite = request.data['favorite']

        new_Pokemon = Pokemon(id = new_id, idUser = new_idUser, name = new_name, type = new_type, move1 = new_move1, move2 = new_move2, move3 = new_move3, srcImg = new_srcImg, favorite = new_favorite)
        new_Pokemon.save()
        
    serialized_pokemon = PokemonSerializer(pokemons, many=True)
    return Response(serialized_pokemon.data)


@api_view(['GET','POST','DELETE'])
def api_postanddelete_user(request, id):
    
    try:
        usuario = User.objects.get(name = id)
    except User.DoesNotExist:
        raise Http404()

    if (request.method == 'DELETE'):
        usuario.delete()
        return Response(status=204)

    serialized_users = UserSerializer(usuario)
    return Response(serialized_users.data)


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
