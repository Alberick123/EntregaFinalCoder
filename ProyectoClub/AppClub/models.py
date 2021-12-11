from django.db import models

class Jugador(models.Model):
    
    nombre = models.CharField(max_length=40)
    altura = models.FloatField()
    edad = models.IntegerField()

class Disciplina(models.Model):
    
    nombre = models.CharField(max_length=40)
    sede = models.CharField(max_length=40)
    dias_realizacion = models.CharField(max_length=40)
    
class Estadio(models.Model):
    
    direccion = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    anioFund = models.IntegerField()
