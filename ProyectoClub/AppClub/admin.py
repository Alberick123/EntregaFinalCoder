from django.contrib import admin
from .models import Avatar, Jugador, Disciplina, Estadio

admin.site.register(Jugador)
admin.site.register(Disciplina)
admin.site.register(Estadio)

admin.site.register(Avatar)
