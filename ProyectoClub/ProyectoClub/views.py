"""
Para definir home en el sitio web
"""

from django.shortcuts import render




def home_view(request):
    
    return render(request, 'AppClub/inicio.html')