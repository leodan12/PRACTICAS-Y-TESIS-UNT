from django.shortcuts import render,redirect

#Modelo y forms
from adminApp.models import Alumno, Practicas
from adminApp.models import Tesis

#Importamos los formularios
from .forms import PracticasForm
from .forms import TesisForm
from django.db.models import Q 

#Paginación
from django.core.paginator import Paginator
from django.http import Http404

#Archivos
#from django.core.files.storage import FileSystemStorage
# Create your views here.

#Usar swal
from django.contrib import messages

 #para verificar el login
from django.contrib.auth.decorators import login_required  
from django.contrib.auth  import logout


#Funciones CRUD para PRACTICAS

def listarPracticas(request): 
    queryset=request.GET.get("buscar")

    author_Name = request.user.first_name 
    author_LastName= request.user.last_name
    alumno=Alumno.objects.get(estado=True, nombres=author_Name, apellidos=author_LastName)

    practicas=Practicas.objects.filter( 
                Q(),estado=True,alumno= alumno.id
                ).distinct()
    page=request.GET.get("page", 1)
    

    try: 
        paginator=Paginator(practicas,4)
        practicas=paginator.page(page)
    except:
        raise Http404
    if queryset:
        practicas=Practicas.objects.filter( 
                Q(lugarPractica__icontains=queryset),estado=True,alumno= alumno.id
                ).distinct()
    context={'entity':practicas,
                'paginator':paginator
            }
    return render(request,"practicas/listaPracticas.html",context)

def agregarPracticas(request): 
    form=PracticasForm()
    author_Name = request.user.first_name 
    author_LastName= request.user.last_name
    alumno=Alumno.objects.get(estado=True, nombres = author_Name, apellidos=author_LastName)
    if request.method=="POST": 
        form=PracticasForm(request.POST,files=request.FILES)
        if form.is_valid():
            practica = Practicas(horasPractica= form.cleaned_data.get('horasPractica'),lugarPractica= form.cleaned_data.get('lugarPractica'),
                fechaInicio= form.cleaned_data.get('fechaInicio'),fechaFinal= form.cleaned_data.get('fechaFinal'),
                porcentajeAvance= form.cleaned_data.get('porcentajeAvance'),informePracticas= form.cleaned_data.get('informePracticas'),
                estadoPractica= form.cleaned_data.get('estadoPractica'),asesorPracticas= form.cleaned_data.get('asesorPracticas'),
                estado=True,alumno=alumno
                )
            practica.save()
         
            messages.success(request,"Guardado correctamente")
            return redirect("listaPracticas")
    else:
        form=PracticasForm()
    context={'form':form}
    return render(request,"practicas/agregar.html",context)

def editarPracticas(request,id): 
    practicas=Practicas.objects.get(id=id)
    if request.method=="POST":
        form=PracticasForm(request.POST,files=request.FILES,instance=practicas) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaPracticas")
    else:
        form=PracticasForm(instance=practicas)
    
    context={"form":form}
    return render(request,"practicas/editar.html",context)

def eliminarPracticas(request,id):
    practica=Practicas.objects.get(id=id)
    practica.estado=False 
    practica.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaPracticas")


#Funciones CRUD para TESIS


def listarTesis(request): 
    queryset=request.GET.get("buscar")

    author_Name = request.user.first_name 
    author_LastName= request.user.last_name
    alumno=Alumno.objects.get(estado=True, nombres = author_Name, apellidos=author_LastName)

    practicas=Practicas.objects.get(estado=True,alumno=alumno.id)

    tesis=Tesis.objects.filter( 
             Q(),estado=True,alumno=alumno.id
             ).distinct()
    page=request.GET.get("page", 1)


    try: 
        paginator=Paginator(tesis,7)
        tesis=paginator.page(page)
    except:
        raise Http404
    if practicas.horasPractica==600: 
        if queryset:
            tesis=Tesis.objects.filter( 
                Q(estadoTesis__icontains=queryset),estado=True,alumno=alumno.id
                ).distinct()
    else:
        messages.error(request,"Tienes que tener 600 horas de prácticas")
        return redirect("homeAlumno")
    context={'entity':tesis,
                'paginator':paginator
                }
    return render(request,"tesis/listaTesis.html",context)

def agregarTesis(request): 
    form=TesisForm()
    author_Name = request.user.first_name 
    author_LastName= request.user.last_name
    alumno=Alumno.objects.get(estado=True, nombres = author_Name, apellidos=author_LastName)
    
    if request.method=="POST": 
        form=TesisForm(request.POST,files=request.FILES)
        if form.is_valid():
            tesis = Tesis(lineaInvestigacion= form.cleaned_data.get('lineaInvestigacion'),nombreTesis= form.cleaned_data.get('nombreTesis'),
                fechaInicio= form.cleaned_data.get('fechaInicio'),fechaFinal= form.cleaned_data.get('fechaFinal'),
                planTesis= form.cleaned_data.get('planTesis'),informeFinal= form.cleaned_data.get('informeFinal'),
                estadoTesis= form.cleaned_data.get('estadoTesis'),asesorTesis= form.cleaned_data.get('asesorTesis'),
                jurado= form.cleaned_data.get('jurado'),
                estado=True,alumno=alumno
                )
            tesis.save()
            messages.success(request,"Guardado correctamente")
            return redirect("listaTesis")
    else:
        form=TesisForm()

    context={'form':form}
    return render(request,"tesis/agregar.html",context)

def editarTesis(request,id): 
    tesis=Tesis.objects.get(id=id)
    if request.method=="POST":
        form=TesisForm(request.POST,instance=tesis,files=request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaTesis")
    else:
        form=TesisForm(instance=tesis)

    context={"form":form}
    return render(request,"tesis/editar.html",context)

def eliminarTesis(request,id):
    tesis=Tesis.objects.get(id=id)
    tesis.estado=False 
    tesis.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaTesis")


#usuario
@login_required(login_url="/")
def homepageAlumno(request):
    username = request.user.username
    author_Name = request.user.first_name 
    author_LastName= request.user.last_name
    alumno=Alumno.objects.get(estado=True, nombres=author_Name, apellidos=author_LastName)
    practicas=Practicas.objects.filter(estado=True,alumno=alumno.id)
    tesis=Tesis.objects.filter(estado=True,alumno=alumno.id)

    context = {'username': username,'practicas': practicas,'tesis': tesis}
    return render(request,"bienvenidoAlumno.html",context)


@login_required(login_url="/")
def salir(request):
    logout(request)
    messages.info(request,"Saliste Exitosamente")
    return redirect("login")
