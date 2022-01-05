from django import forms
import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserEditForm(UserCreationForm):

    #Obligatorios
    email = forms.EmailField(label="Ingrese su email:")
    password1 = forms.CharField(label='Contraseña')
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
    
    #class Meta:
    #   model = User
    #   fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
    #  help_texts = {k:"" for k in fields}

class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    #Extra
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre',localize=0)

    #imagen_avatar = forms.ImageField(required=False)


    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
    
    
    #class Meta:
    #   model = User
    #   fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        #Saca los mensajes de ayuda
    #  help_texts = {k:"" for k in fields}




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


