from django.urls import path
from AppClub import views

urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
    path('plantel', views.plantel, name="Plantel"),
    path('disciplinas', views.disciplinas, name="Disciplinas"),
    path('estadio', views.estadio, name="Estadio"),
    path('estadio/list', views.EstadioList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.EstadioDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EstadioCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EstadioUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EstadioDelete.as_view(), name='Delete'),
    
    
]