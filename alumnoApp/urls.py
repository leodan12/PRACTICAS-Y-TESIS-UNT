from SeguridadApp.views import homepageAlumno
from .views import listarPracticas,agregarPracticas,editarPracticas,eliminarPracticas
from .views import listarTesis,agregarTesis,editarTesis,eliminarTesis
from .views import salir,homepageAlumno
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    #Practicas
    path('listaPracticas/',listarPracticas,name="listaPracticas"),
    path('agregarPracticas/',agregarPracticas,name="agregarPracticas"),
    path('editarPracticaAlumno/<int:id>/',editarPracticas,name="editarPracticasAlumno"),
    path('eliminarPractica/<int:id>/',eliminarPracticas,name="eliminarPracticas"),

    #Tesis
    path('listaTesis/',listarTesis,name="listaTesis"),
    path('agregarTesis/',agregarTesis,name="agregarTesis"),
    path('editarTesisAlumno/<int:id>/',editarTesis,name="editarTesisAlumno"),
    path('eliminarTesis/<int:id>/',eliminarTesis,name="eliminarTesis"),

    #Para Rol
    path('Alumno/',homepageAlumno,name="homeAlumno"),
    path('logout/',salir,name="logout"),
]