from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/users/', views.api_getandpost_users, name='all_users'),
    path('api/users/<id>', views.api_postanddelete_user, name='postedelete')
]