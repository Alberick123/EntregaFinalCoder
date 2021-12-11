from django.shortcuts import render

from django.http import HttpResponse

def inicio(request):
    
    return render(request, 'AppClub/inicio.html')


def plantel(request):
    
    return render(request, 'AppClub/plantel.html')


def disciplinas(request):
    
    return render(request, 'AppClub/disciplinas.html')

def estadio(request):

    return render(request, 'AppClub/estadio.html')
