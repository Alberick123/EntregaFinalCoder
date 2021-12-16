from django import forms
import datetime

class EstadioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    anioFund = forms.DateField(initial=datetime.date.today)


class DisciplinaForm(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    sede = forms.CharField(max_length=40)
    dias_realizacion = forms.DateField()


class JugadorForm(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    altura = forms.FloatField()
    edad = forms.IntegerField()