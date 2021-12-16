from django.shortcuts import render

from django.http import HttpResponse
from .forms import EstadioForm, DisciplinaForm, JugadorForm
from .models import Estadio, Jugador, Disciplina

def inicio(request):
    
    return render(request, 'AppClub/inicio.html')


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


