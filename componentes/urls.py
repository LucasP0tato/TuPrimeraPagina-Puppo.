from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar-procesador/', views.agregar_procesador, name='agregar_procesador'),
    path('buscar-procesador/', views.buscar_procesador, name='buscar_procesador'),
]
