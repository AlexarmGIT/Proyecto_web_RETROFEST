from django.shortcuts import render
from retro_fest.models import Organizadores 
from retro_fest.models import Amigos 
from retro_fest.models import Punto_de_venta 
from django.http import HttpResponse
from retro_fest.forms  import Organizadores1
from retro_fest.forms  import Amigos1
from retro_fest.forms  import Punto_de_venta1
import datetime

# Create your views here.


def inicio(request):
    return render (request , "inicio.html")


def anotate(request):
   
 if request.method == "POST":

         formulario_Org = Organizadores1 ( request.POST )

         if formulario_Org.is_valid():
            datos = formulario_Org.cleaned_data
            nueva = Organizadores(nombre =datos['nombre'] , puesto = datos['puesto'] , edad = datos['edad'])
            nueva.save()
            return render( request , "sumate.html")  
 return render( request , "sumate.html")


def anotate1(request):
   
    if request.method == "POST":
        formulario_Ami = Amigos1 ( request.POST)

        if formulario_Ami.is_valid():
            datos1 = formulario_Ami.cleaned_data
            nueva = Amigos(nombre = datos1['nombre'] , marca =datos1['marca'] , cuit = datos1['cuit'])
            nueva.save()
        return render( request , "sumate.html")  
 
    return render(request , "sumate.html")


def anotate2(request):
    
    if request.method == "POST":
        formulario_Ami = Punto_de_venta1 ( request.POST )

        if formulario_Ami.is_valid():
            datos2 = formulario_Ami.cleaned_data
            nueva = Punto_de_venta(nombre = datos2['nombre'] , apellido = datos2['apellido'] , dni = datos2['dni'])
            nueva.save()
            return render( request , "sumate.html")  
 
    return render(request , "sumate.html")





def lista_familia (request):

    familiares = Organizadores.objects.all()
    datos = {"datos" : familiares }   

    return render (request , "lista_invitados.html" , datos)


def alta_familiares (request):
    familiar = Organizadores( nombre= "Paz" , puesto= "Gerente comercial" , edad=24 )
    familiar.save()
    familiar = Organizadores( nombre= "Alfonsina" , puesto= "Eventos"  , edad=21 )
    familiar.save()
    familiar = Organizadores( nombre= "Antonella" , puesto= "Presidente" , edad=31 )
    familiar.save()

def lista_amigos (request):
    amistades = Amigos.objects.all()
    amistad = {"amistad" : amistades }   

    return render (request , "lista_invitados.html" , amistad)


def alta_amistades (request):
    amistad = Amigos( nombre= "Martin" , marca= "Quilmes" , cuit= 1)
    amistad.save()
    amistad = Amigos( nombre= "Fidel" , marca= "Branca" , cuit= 332 )
    amistad.save()
    amistad = Amigos( nombre= "Augusto" , marca= "Paty" , cuit= 33 )
    amistad.save()

def lista_conocidos (request):
    compinches = Punto_de_venta.objects.all()
    datos2 = {"datos2" : compinches }   

    return render (request , "lista_invitados.html" , datos2)



def alta_conocidos (request):
    conocido = Punto_de_venta( nombre= "Marcos" , apellido="Lopez" , dni= 333444333 )
    conocido.save()
    conocido = Punto_de_venta( nombre= "lucas" , apellido= " Gym toros" , dni = 32333222 )
    conocido.save() 
    conocido = Punto_de_venta( nombre="pablo" , aplellido= "Drugtore M" , dni = 31455221)
    conocido.save()




def confirma_asistencia(request):
      return render (request ,"confirma_asistencia.html")    



def buscar (request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        alta_conocidos = Punto_de_venta.objects.filter(nombre__icontains = nombre)
        return render ( request , "resultado_busqueda.html" , {"alta_conocidos":alta_conocidos})
    else:
        return HttpResponse("no ingresaste ningun campo ")    



    return HttpResponse()
    
