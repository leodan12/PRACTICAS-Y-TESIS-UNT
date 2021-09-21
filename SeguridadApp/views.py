from django import forms
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q 

from .models import Perfil
from adminApp.models import AsesorTesis,AsesorPracticas,Alumno,Carrera, LineaInvestigacion, Tesis
from .models import guardar_usuario_perfil

from django.views.generic import CreateView, TemplateView
from .forms import  SignUpForm
# Create your views here.


    

#@login_required(login_url="/")
def acceder(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario,password=password)
            if usuario is not None:
                login(request,usuario)
                usuario1=User.objects.get(username=nombre_usuario)
                perfil=Perfil.objects.get(usuario=usuario1)
                if perfil.rol == "asesor":
                    return redirect("homeAsesor")
                elif perfil.rol == "alumno":
                    return redirect("homeAlumno")
                elif perfil.rol == "administrador" :
                    return redirect("homeAdmin")
                
            else:
                messages.error(request,"los datos son incorrectos")
        else:
            messages.error(request,"los datos son incorrectos")

    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def registrar(request):
    model=Perfil
    form=SignUpForm()
    if request.method=="POST": 
        form=SignUpForm(request.POST)
        if form.is_valid():
            
            form.save()
            usuario0 = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario1=User.objects.get(username=usuario0)
            perfil=Perfil.objects.get(usuario=usuario1)
            perfil.rol=form.cleaned_data.get('rol')
            perfil.save()

            usuario = authenticate(username=usuario0, password=password)
            perf=form.cleaned_data.get('rol')
            if perf == "asesor" :
                asesorT = AsesorTesis(asesorTesis= form.cleaned_data.get('first_name') +" "+ form.cleaned_data.get('last_name') )
                asesorT.save()

                asesorP = AsesorPracticas(asesorPracticas= form.cleaned_data.get('first_name') +" "+ form.cleaned_data.get('last_name') )
                asesorP.save()
                if usuario is not None:
                    login(request,usuario)
                return redirect("homeAsesor")

            if perf == "alumno":
                carrera=Carrera.objects.get(id = 1)
                alumno = Alumno(nombres= form.cleaned_data.get('first_name'),apellidos= form.cleaned_data.get('last_name'),
                correoUnitru= form.cleaned_data.get('email'),celular= "987654321",carreras = carrera)
               
                alumno.save()
                if usuario is not None:
                    login(request,usuario)
                return redirect("homeAlumno") 
                
            
                   
    context={'form':form}
    return render(request,"registrar.html",context)

   

@login_required(login_url="/")
def homepage(request):
    username = request.user.username
    context = {'username': username}
     
    return render(request,"inicio.html",context)

@login_required(login_url="/")
def homepageAlumno(request):
    username = request.user.username
    context = {'username': username}
     
    return render(request,"bienvenidoAlumno.html",context)

@login_required(login_url="/")
def homepageAdmin(request):
    username = request.user.username
    context = {'username': username}
     
    return render(request,"bienvenidoAdmin.html",context)

@login_required(login_url="/")
def salir(request):
    logout(request)
    messages.info(request,"Saliste Exitosamente")
    return redirect("login")




def tesisAprobadas(request):
       
    Lineas_Investigacion=LineaInvestigacion.objects.filter( estado=True)
    tesis=Tesis.objects.filter( lineaInvestigacion=Lineas_Investigacion,estado=True).distinct() 

    context = {'Lineas_Investigacion': Lineas_Investigacion, 'tesis':tesis}
    return render(request,"LineasInvestigacion.html",context)





def VerTesisDisponibles(request,id):
    queryset=request.GET.get("buscar")
      
    #Lineas_Investigacion=LineaInvestigacion.objects.filter( estado=True)

    Linea=LineaInvestigacion.objects.get(estado=True,id=id)

    tesis=Tesis.objects.filter(lineaInvestigacion=Linea)
    if queryset:
        tesis=Tesis.objects.filter(
            Q(nombreTesis__icontains=queryset),estado=True
        ).distinct() 

    numero=tesis.count()

    context = {'Linea': Linea,'tesis': tesis,'numero': numero}
    return render(request,"listaTesisAprobadas.html",context)




