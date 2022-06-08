from django.db import models

# Create your models here.


class Organizadores(models.Model):

        nombre = models.CharField(max_length=30)
        puesto = models.CharField(max_length=30)
        edad = models.IntegerField()

class Amigos (models.Model):
        nombre = models.CharField(max_length=30)
        marca = models.CharField(max_length=30)
        cuit = models.IntegerField()

class Punto_de_venta (models.Model):
        nombre = models.CharField(max_length=30)
        apellido = models.CharField(max_length=30)
        dni = models.IntegerField()    

