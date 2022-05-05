from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import User

from .serializers import UserSerializer

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

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
