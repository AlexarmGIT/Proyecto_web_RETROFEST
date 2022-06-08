"""proyecto_entregable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path , include
from retro_fest import views


urlpatterns = [
    
    path("", views.inicio, name="inicio" ),
    path("lista_familia/",views.lista_familia , name="lista_familia"),
    path("lista_amigos/",views.lista_amigos , name="lista_amigos"),
    path("lista_conocidos/",views.lista_conocidos),
    path('admin/', admin.site.urls), 
    path("retro_fest/", include ("retro_fest.urls")),
    path("anotate/", views.anotate, name="anotate"),
    path("anotate/anotate", views.anotate, name="anotate"),
    path("anotate/anotate1", views.anotate1, name="anotate1"),
    path("anotate/anotate2", views.anotate2, name="anotate2"),
    path("confirma_asistencia" , views.confirma_asistencia, name="confirma_asistencia"),
    path("buscar" , views.buscar, )


    ]
