from django.shortcuts import render

from django.http import HttpResponse, request
from .forms import EstadioForm, DisciplinaForm, JugadorForm, UserRegisterForm
from .models import Estadio, Jugador, Disciplina
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.defaults import page_not_found



def inicio(request):
    
    return render(request, 'AppClub/inicio.html')

def contacto(request):
    
    return render(request, 'AppClub/contacto.html')

def terminos(request):
    
    return render(request, 'AppClub/terminos.html')

def privacidad(request):
    
    return render(request, 'AppClub/privacidad.html')

def acercade(request):
    
    return render(request, 'AppClub/acercade.html')


def plantel(request):
    if request.method == "POST":
        formularioJugadores = JugadorForm(request.POST)
        if formularioJugadores.is_valid():
            informacion = formularioJugadores.cleaned_data
            jugadores = Jugador()
            jugadores.nombre = informacion['nombre']
            jugadores.altura = informacion['altura']
            jugadores.edad = informacion['edad']
            jugadores.save()
    else:
        formularioJugadores = JugadorForm()    
    return render(request, 'AppClub/plantel.html')


def disciplinas(request):
    if request.method == "POST":
        formularioDisciplina = DisciplinaForm(request.POST)
        if formularioDisciplina.is_valid():
            informacion = formularioDisciplina.cleaned_data
            disciplinas = Disciplina()
            disciplinas.nombre = informacion['nombre']
            disciplinas.sede = informacion['sede']
            disciplinas.dias_realizacion = informacion['dias_realizacion']
            disciplinas.save()
    else:
        formularioDisciplina = DisciplinaForm()
    return render(request, 'AppClub/disciplinas.html')

def estadio(request):
    if request.method == "POST":
        formularioEstadio = EstadioForm(request.POST)
        if formularioEstadio.is_valid():
            informacion = formularioEstadio.cleaned_data
            estadio = Estadio()
            estadio.nombre = informacion['nombre']
            estadio.direccion = informacion['direccion']
            estadio.anioFund = informacion['anioFund']
            estadio.save()
    else:
        formularioEstadio = EstadioForm()

    return render(request, 'AppClub/estadio.html')

#@login_required
class EstadioList(LoginRequiredMixin, ListView):

    model = Estadio
    template_name = "AppClub/estadios_list.html"

class EstadioDetalle(LoginRequiredMixin, DetailView):

    model = Estadio
    template_name = "AppClub/estadio_detalle.html"

class EstadioCreacion(LoginRequiredMixin, CreateView):

    model = Estadio
    success_url = "/AppClub/estadio/list"
    fields = ['nombre', 'direccion', 'anioFound']

class EstadioUpdate(LoginRequiredMixin, UpdateView):

    model = Estadio
    success_url = "/AppClub/estadio/list"
    fields = ['nombre', 'direccion', 'anioFund']

class EstadioDelete(LoginRequiredMixin, DeleteView):

    model = Estadio
    success_url = "/AppClub/estadio/list"

class JugadorList(LoginRequiredMixin, ListView):

    model = Jugador
    template_name = "AppClub/plantel_list.html"

class JugadorDetalle(LoginRequiredMixin, DetailView):

    model = Jugador
    template_name = "AppClub/plantel_detalle.html"

class JugadorCreacion(LoginRequiredMixin, CreateView):

    model = Jugador
    success_url = "/AppClub/plantel/list"
    fields = ['nombre', 'altura', 'edad']

class JugadorUpdate(LoginRequiredMixin, UpdateView):

    model = Jugador
    success_url = "/AppClub/plantel/list"
    fields = ['nombre', 'altura', 'edad']

class JugadorDelete(LoginRequiredMixin, DeleteView):

    model = Jugador
    success_url = "/AppClub/plantel/list"

class DisciplinaList(LoginRequiredMixin, ListView):

    model = Disciplina
    template_name = "AppClub/disciplinas_list.html"

class DisciplinaDetalle(LoginRequiredMixin, DetailView):

    model = Disciplina
    template_name = "AppClub/disciplinas_detalle.html"

class DisciplinaCreacion(LoginRequiredMixin, CreateView):

    model = Disciplina
    success_url = "/AppClub/disciplinas/list"
    fields = ['nombre', 'sede', 'dias_realizacion']

class DisciplinaUpdate(LoginRequiredMixin, UpdateView):

    model = Disciplina
    success_url = "/AppClub/disciplinas/list"
    fields = ['nombre', 'sede', 'dias_realizacion']

class DisciplinaDelete(LoginRequiredMixin, DeleteView):

    model = Disciplina
    success_url = "/AppClub/disciplinas/list"

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                
                return render(request,"AppClub/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
            else:
                return render(request,"AppClub/inicio.html", {"mensaje":"Error en los datos ingresados"})

        else:
            return render(request,"AppClub/inicio.html", {"mensaje":"Error formulario erroneo"})

    form = AuthenticationForm()

    return render (request,"AppClub/login.html", {'form':form})


def register(request):
    
    if request.method == 'POST':
        
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppClub/inicio.html", {"mensaje":f"{username} creado"})
    else:
        form = UserRegisterForm()
    
    return render(request,"AppClub/registro.html", {"form":form})