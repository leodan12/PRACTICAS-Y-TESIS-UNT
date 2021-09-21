from django import forms
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from alumnoApp.models import Alumno
from adminApp.models import AsesorPracticas
from adminApp.models import AsesorTesis
from adminApp.models import Practicas
from adminApp.models import Tesis
from django.db.models import Q 
 
 #importamos los formularios
from .forms import PracticasForm
from .forms import TesisForm
#importamos lo necesario para trabajar con pdf

from django.contrib.auth.decorators import login_required  #para verificar el login
   

# VISTAS PARA PRACTICAS
def ListaPracticantes(request):
    queryset=request.GET.get("buscar")
    practicantes=Practicas.objects.filter(estado=True)

    author = request.user.first_name + " " + request.user.last_name
    asesor=AsesorPracticas.objects.get(estado=True, asesorPracticas = author)
     
    practicas=Practicas.objects.filter(
            Q(),estado=True,asesorPracticas = asesor.id
        ).distinct()
    context={'practicas':practicas}
    return render(request,"practicasAsesor/listaPracticantes.html",context)

def editarPractica(request,id):
    practica=Practicas.objects.get(id=id)
    if request.method=="POST":
        form=PracticasForm(request.POST,instance=practica,files=request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect("ListaPracticantes")
    else:
        form=PracticasForm(instance=practica)
 
    context={"form":form}
    return render(request,"practicasAsesor/editar.html",context)


#VISTAS PARA TESIS
def ListaTesistas(request):
    queryset=request.GET.get("buscar")
    
    author = request.user.first_name + " " + request.user.last_name
    asesor=AsesorTesis.objects.get(estado=True, asesorTesis = author)
    tesistas=Tesis.objects.filter( estado=True)
    
    tesis=Tesis.objects.filter(
            Q( ),estado=True,asesorTesis=asesor.id
        ).distinct()
    context={'tesis':tesis}
    return render(request,"tesisAsesor/listaTesistas.html",context)


def editarTesis(request,id):
    tesis=Tesis.objects.get(id=id)
    if request.method=="POST":
        form=TesisForm(request.POST,instance=tesis,files=request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect("ListaTesistas")
    else:
        form=TesisForm(instance=tesis)
 
    context={"form":form}
    return render(request,"tesisAsesor/editar.html",context)


#usuario
@login_required(login_url="/")
def homepage(request):
    username = request.user.username
    context = {'username': username}
     
    return render(request,"inicio.html",context)


@login_required(login_url="/")
def salir(request):
    logout(request)
    messages.info(request,"Saliste Exitosamente")
    return redirect("login")
