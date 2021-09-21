from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from AsesoresApp.views import homepage,salir,ListaPracticantes,ListaTesistas,editarPractica,editarTesis

urlpatterns =[
    #para practicas
    path('ListaPracticantes/',ListaPracticantes,name="ListaPracticantes"),
    path('editarPracticaAsesor/<int:id>/',editarPractica,name="editarPractica"),

    #para tesis
    path('ListaTesistas/',ListaTesistas,name="ListaTesistas"),
    path('editarTesis/<int:id>/',editarTesis,name="editarTesis"),
    path('Asesor/',homepage,name="homeAsesor"),
    path('logout/',salir,name="logout"),
]