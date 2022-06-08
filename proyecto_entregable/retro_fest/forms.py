from django import forms




class Organizadores1(forms.Form):

        nombre = forms.CharField(max_length=30)
        puesto = forms.CharField(max_length=30)
        edad = forms.IntegerField()

class Amigos1(forms.Form):
        nombre = forms.CharField(max_length=30)
        marca = forms.CharField(max_length=30)
        cuit = forms.IntegerField()

class Punto_de_venta1(forms.Form):
        nombre = forms.CharField(max_length=30)
        apellido = forms.CharField(max_length=30)
        dni = forms.IntegerField()    

 