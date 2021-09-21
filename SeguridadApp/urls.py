from django.contrib import admin
from django.urls import path
from django.urls.resolvers import URLPattern
from SeguridadApp.views import acceder,salir,registrar,homepageAlumno,homepageAdmin,tesisAprobadas,VerTesisDisponibles

urlpatterns =[
    path('',acceder,name="login"),
    path('registro/',registrar,name="registrar"),

    path('homeAlumno/',homepageAlumno,name="homeAlumno"),
    path('homeAdmin/',homepageAdmin,name="homeAdmin"),
    path('logout/',salir,name="logout"),

    #ver tesis disponibles
    path('Tesis_Aprobadas/',tesisAprobadas,name="tesisAprobadas"),
    path('VerTesisDisponibles/<int:id>/',VerTesisDisponibles,name="VerTesisDisponibles"),

]