from adminApp.models import AsesorPracticas
from SeguridadApp.views import homepageAlumno
from .views import agregarPerfil, editarPerfil, eliminarPerfil, listarFacultad,agregarFacultad,editarFacultad,eliminarFacultad, listarPerfil
from .views import listarCarrera,agregarCarrera,editarCarrera,eliminarCarrera
from .views import listarAlumno,editarAlumno,agregarAlumno,eliminarAlumno
from .views import listarAsesorPracticas,editarAsesorPracticas,agregarAsesorPracticas,eliminarAsesorPracticas
from .views import listarPracticasAdmin,agregarPracticas,editarPracticas,eliminarPracticas
from .views import listarAsesorTesis,agregarAsesorTesis,editarAsesorTesis,eliminarAsesorTesis
from .views import listarJurado,agregarJurado,editarJurado,eliminarJurado
from .views import listarLineaInv,agregarLineaInv,editarLineaInv,eliminarLineaInv
from .views import listarTesisAdmin,agregarTesisAdmin,editarTesisAdmin,eliminarTesisAdmin

from .views import salir,homepageAdmin
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    #Facultad
    path('listaFacultad/',listarFacultad,name="listaFacultad"),
    path('agregarFacultad/',agregarFacultad,name="agregarFacultad"),
    path('editarFacultad/<int:id>/',editarFacultad,name="editarFacultad"),
    path('eliminarFacultad/<int:id>/',eliminarFacultad,name="eliminarFacultad"),

    #Carrera
    path('listaCarrera/',listarCarrera,name="listaCarrera"),
    path('agregarCarrera/',agregarCarrera,name="agregarCarrera"),
    path('editarCarrera/<int:id>/',editarCarrera,name="editarCarrera"),
    path('eliminarCarrera/<int:id>/',eliminarCarrera,name="eliminarCarrera"),

    #Alumno
    path('listaAlumno/',listarAlumno,name="listaAlumno"),
    path('agregarAlumno/',agregarAlumno,name="agregarAlumno"),
    path('editarAlumno/<int:id>/',editarAlumno,name="editarAlumno"),
    path('eliminarAlumno/<int:id>/',eliminarAlumno,name="eliminarAlumno"),

    #Asesor de Prácticas
    path('listaAsesorPractica/',listarAsesorPracticas,name="listaAsesorPractica"),
    path('agregarAsesorPractica/',agregarAsesorPracticas,name="agregarAsesorPractica"),
    path('editarAsesorPractica/<int:id>/',editarAsesorPracticas,name="editarAsesorPractica"),
    path('eliminarAsesorPractica/<int:id>/',eliminarAsesorPracticas,name="eliminarAsesorPractica"),

    #Practicas
    path('listaPracticasAdmin/',listarPracticasAdmin,name="listaPracticasAdmin"),
    path('agregarPracticasAdmin/',agregarPracticas,name="agregarPracticasAdmin"),
    path('editarPracticasAdmin/<int:id>/',editarPracticas,name="editarPracticasAdmin"),
    path('eliminarPracticasAdmin/<int:id>/',eliminarPracticas,name="eliminarPracticasAdmin"),

    #Jurado
    path('listaJurado/',listarJurado,name="listaJurado"),
    path('agregarJurado/',agregarJurado,name="agregarJurado"),
    path('editarJurado/<int:id>/',editarJurado,name="editarJurado"),
    path('eliminarJurado/<int:id>/',eliminarJurado,name="eliminarJurado"),

    #Linea de Inv.
    path('listaLineaInv/',listarLineaInv,name="listaLineaInv"),
    path('agregarLineaInv/',agregarLineaInv,name="agregarLineaInv"),
    path('editarLineaInv/<int:id>/',editarLineaInv,name="editarLineaInv"),
    path('eliminarLineaInv/<int:id>/',eliminarLineaInv,name="eliminarLineaInv"),

    #Asesor de Tesis
    path('listaAsesorTesis/',listarAsesorTesis,name="listaAsesorTesis"),
    path('agregarAsesorTesis/',agregarAsesorTesis,name="agregarAsesorTesis"),
    path('editarAsesorTesis/<int:id>/',editarAsesorTesis,name="editarAsesorTesis"),
    path('eliminarAsesorTesis/<int:id>/',eliminarAsesorTesis,name="eliminarAsesorTesis"),

    #Tesis
    path('listaTesisAdmin/',listarTesisAdmin,name="listaTesisAdmin"),
    path('agregarTesisAdmin/',agregarTesisAdmin,name="agregarTesisAdmin"),
    path('editarTesisAdmin/<int:id>/',editarTesisAdmin,name="editarTesisAdmin"),
    path('eliminarTesisAdmin/<int:id>/',eliminarTesisAdmin,name="eliminarTesisAdmin"),

    #Perfil
    path('listaPerfil/',listarPerfil,name="listaPerfil"),
    path('agregarPerfil/',agregarPerfil,name="agregarPerfil"),
    path('editarPerfil/<int:id>/',editarPerfil,name="editarPerfil"),
    path('eliminarPerfil/<int:id>/',eliminarPerfil,name="eliminarPerfil"),

    #Para Rol
    path('Admin/',homepageAdmin,name="homeAdmin"),
    path('logout/',salir,name="logout"),
]