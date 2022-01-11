from django.db import models

from django.contrib.auth.models import User
from django.db.models.fields.files import ImageField

class Jugador(models.Model):
    
    nombre = models.CharField(max_length=40)
    altura = models.FloatField()
    edad = models.IntegerField()
    
    def __str__(self):
        return "{} - {}".format(self.nombre, self.altura)

class Disciplina(models.Model):
    
    nombre = models.CharField(max_length=40)
    sede = models.CharField(max_length=40)
    dias_realizacion = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.nombre, self.sede)
    
class Estadio(models.Model):
    nombre = models.CharField(max_length=40)    
    direccion = models.CharField(max_length=40)
    anioFund = models.DateField()

    def __str__(self):
        return "{} - {}".format(self.nombre, self.direccion)
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    imagen = models.ImageField(upload_to='avatares', null = True, blank = True)
    
