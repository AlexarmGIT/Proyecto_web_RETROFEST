from django.urls import path
from . import views





urlpatterns = [

    path("lista_familia" , views.lista_familia),
    path("alta_familiares" , views.alta_familiares),
    path("lista_amigos", views.lista_amigos),
    path("alta_amistades" , views.alta_amistades),
    path("lista_conocidos" , views.lista_conocidos),
    path("alta_conocidos" , views.alta_conocidos)

 ]