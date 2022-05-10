from django.http import HttpResponse
from numpy import logical_and, logical_not
from pkg_resources import get_supported_platform
from requests import put

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User

from .serializers import UserSerializer



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
            return Response(status=200, data = {'logged_in': True})
        except:
            return Response(status=404)

    else:
        return Response(status=200, data = {'aviso': 'esperando post para verificação do usuario'})
        
    
# /users/register
@api_view(['POST'])
def register(request):
    new_name = request.data['name']
    new_password = request.data['password']

    new_User = User(name = new_name, password = new_password)
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

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
