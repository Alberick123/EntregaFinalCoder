from django.urls import path
from AppClub import views

urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
    path('plantel', views.plantel, name="Plantel"),
    path('disciplinas', views.disciplinas, name="Disciplinas"),
    path('estadio', views.estadio, name="Estadio"),
]