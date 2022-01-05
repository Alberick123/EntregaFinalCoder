from django.urls import path
from AppClub import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
    path('plantel', views.plantel, name="Plantel"),
    path('disciplinas', views.disciplinas, name="Disciplinas"),
    path('contacto', views.contacto, name="Contacto"),
    path('terminos', views.terminos, name="Terminos"),
    path('privacidad', views.privacidad, name="Privacidad"),
    path('acercade', views.acercade, name="AcercaDe"),
    path('estadio', views.estadio, name="Estadio"),
    path('estadio/list', views.EstadioList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.EstadioDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EstadioCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EstadioUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EstadioDelete.as_view(), name='Delete'),
    path('plantel/list', views.JugadorList.as_view(), name='List2'),
    path(r'^2(?P<pk>\d+)$', views.JugadorDetalle.as_view(), name='Detail2'),
    path(r'^nuevo2$', views.JugadorCreacion.as_view(), name='New2'),
    path(r'^editar2/(?P<pk>\d+)$', views.JugadorUpdate.as_view(), name='Edit2'),
    path(r'^borrar2/(?P<pk>\d+)$', views.JugadorDelete.as_view(), name='Delete2'),
    path('disciplinas/list', views.DisciplinaList.as_view(), name='List3'),
    path(r'^3(?P<pk>\d+)$', views.DisciplinaDetalle.as_view(), name='Detail3'),
    path(r'^nuevo3$', views.DisciplinaCreacion.as_view(), name='New3'),
    path(r'^editar3/(?P<pk>\d+)$', views.DisciplinaUpdate.as_view(), name='Edit3'),
    path(r'^borrar3/(?P<pk>\d+)$', views.DisciplinaDelete.as_view(), name='Delete3'),
    
    #Login - Logout - Register
    path('login', views.login_request, name = 'Login' ),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='AppClub/logout.html'), name = 'Logout'),
]