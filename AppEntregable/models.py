from os import link
from django.db import models
#Clase de usuario
class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    nombre_de_usuario=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    fecha_de_nacimiento=models.DateField()
    def __str__(self):
        return self.nombre+" "+str(self.apellido)+" "+str(self.nombre_de_usuario)

class Bibliotecas(models.Model):
    nombre = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    direccion = models.CharField(max_length=60)
    apertura = models.CharField(max_length=100)
    link = models.URLField(max_length=200, blank=True, null=True)
    imagen = models.URLField(max_length=300, blank=True, null=True)
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre_libro = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    link_autor = models.URLField(max_length=200, blank=True, null=True)
    link_texto = models.URLField(max_length=200, blank=True, null=True)
    descripcion = models.CharField(max_length=1000)
    def __str__(self):
        return self.nombre_libro+" "+str(self.autor)