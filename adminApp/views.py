from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate,login,logout
#Modelo y forms
from adminApp.models import Alumno, Practicas,AsesorPracticas,AsesorTesis,Carrera,Facultad,Jurado,LineaInvestigacion,Tesis

#Importamos los formularios
from .forms import PracticasForm,TesisForm,AlumnoForm,FacultadForm,CarreraForm,AsesorPracticasForm,AsesorTesisForm,JuradoForm,LineaInvestigacionForm


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


#CRUD para FACULTAD

def listarFacultad(request): 
    queryset=request.GET.get("buscar")
    facultad=Facultad.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(facultad,7)
        facultad=paginator.page(page)
    except:
        raise Http404
    if queryset:
         facultad=Facultad.objects.filter( 
             Q(facultad__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':facultad,
                'paginator':paginator}
    return render(request,"facultad/lista.html",context)


def agregarFacultad(request): 
    form=FacultadForm()
    if request.method=="POST": 
        form=FacultadForm(request.POST)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaFacultad")
    else:
        form=FacultadForm()
    context={'form':form}
    return render(request,"facultad/agregar.html",context)


def editarFacultad(request,id): 
    facultad=Facultad.objects.get(id=id)
    if request.method=="POST":
        form=FacultadForm(request.POST,instance=facultad) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaFacultad")
    else:
        form=FacultadForm(instance=facultad)
    
    context={"form":form}
    return render(request,"facultad/editar.html",context)

def eliminarFacultad(request,id):
    facultad=Facultad.objects.get(id=id)
    facultad.estado=False 
    facultad.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaFacultad")

#CRUD para CARRERA

def listarCarrera(request): 
    queryset=request.GET.get("buscar")
    carrera=Carrera.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(carrera,7)
        carrera=paginator.page(page)
    except:
        raise Http404
    if queryset:
         carrera=Carrera.objects.filter( 
             Q(carrera__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':carrera,
                'paginator':paginator}
    return render(request,"carrera/lista.html",context)


def agregarCarrera(request): 
    form=CarreraForm()
    if request.method=="POST": 
        form=CarreraForm(request.POST)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaCarrera")
    else:
        form=CarreraForm()
    context={'form':form}
    return render(request,"carrera/agregar.html",context)


def editarCarrera(request,id): 
    carrera=Carrera.objects.get(id=id)
    if request.method=="POST":
        form=CarreraForm(request.POST,instance=carrera) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaCarrera")
    else:
        form=CarreraForm(instance=carrera)
    
    context={"form":form}
    return render(request,"carrera/editar.html",context)

def eliminarCarrera(request,id):
    carrera=Carrera.objects.get(id=id)
    carrera.estado=False 
    carrera.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaCarrera")

#CRUD para Alumno

def listarAlumno(request): 
    queryset=request.GET.get("buscar")
    alumno=Alumno.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(alumno,7)
        alumno=paginator.page(page)
    except:
        raise Http404
    if queryset:
         alumno=Alumno.objects.filter( 
             Q(apellidos__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':alumno,
                'paginator':paginator}
    return render(request,"alumno/lista.html",context)


def agregarAlumno(request): 
    form=AlumnoForm()
    if request.method=="POST": 
        form=AlumnoForm(request.POST)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaAlumno")
    else:
        form=AlumnoForm()
    context={'form':form}
    return render(request,"alumno/agregar.html",context)


def editarAlumno(request,id): 
    alumno=Alumno.objects.get(id=id)
    if request.method=="POST":
        form=AlumnoForm(request.POST,instance=alumno) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaAlumno")
    else:
        form=AlumnoForm(instance=alumno)
    
    context={"form":form}
    return render(request,"alumno/editar.html",context)

def eliminarAlumno(request,id):
    alumno=Alumno.objects.get(id=id)
    alumno.estado=False 
    alumno.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaAlumno")

#CRUD para Asesor practicas


def listarAsesorPracticas(request): 
    queryset=request.GET.get("buscar")
    asesorPracticas=AsesorPracticas.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(asesorPracticas,7)
        asesorPracticas=paginator.page(page)
    except:
        raise Http404
    if queryset:
         asesorPracticas=AsesorPracticas.objects.filter( 
             Q(asesorPracticas__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':asesorPracticas,
                'paginator':paginator}
    return render(request,"asesorPracticasAdmin/lista.html",context)


def agregarAsesorPracticas(request): 
    form=AsesorPracticasForm()
    if request.method=="POST": 
        form=AsesorPracticasForm(request.POST)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaAsesorPractica")
    else:
        form=AsesorPracticasForm()
    context={'form':form}
    return render(request,"asesorPracticasAdmin/agregar.html",context)


def editarAsesorPracticas(request,id): 
    asesorPractica=AsesorPracticas.objects.get(id=id)
    if request.method=="POST":
        form=AsesorPracticasForm(request.POST,instance=asesorPractica) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaAsesorPractica")
    else:
        form=AsesorPracticasForm(instance=asesorPractica)
    
    context={"form":form}
    return render(request,"asesorPracticasAdmin/editar.html",context)

def eliminarAsesorPracticas(request,id):
    asesorPracticas=AsesorPracticas.objects.get(id=id)
    asesorPracticas.estado=False 
    asesorPracticas.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaAsesorPractica")

#Funciones CRUD para PRACTICAS

def listarPracticasAdmin(request): 
    queryset=request.GET.get("buscar")
    practicas=Practicas.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(practicas,7)
        practicas=paginator.page(page)
    except:
        raise Http404
    if queryset:
         practicas=Practicas.objects.filter( 
             Q(lugarPractica__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':practicas,
                'paginator':paginator}
    return render(request,"practicasAdmin/lista.html",context)


def agregarPracticas(request): 
    form=PracticasForm()
    if request.method=="POST": 
        form=PracticasForm(request.POST,files=request.FILES)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaPracticasAdmin")
    else:
        form=PracticasForm()
    context={'form':form}
    return render(request,"practicasAdmin/agregar.html",context)


def editarPracticas(request,id): 
    practicas=Practicas.objects.get(id=id)
    if request.method=="POST":
        form=PracticasForm(request.POST,files=request.FILES,instance=practicas) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaPracticasAdmin")
    else:
        form=PracticasForm(instance=practicas)
    
    context={"form":form}
    return render(request,"practicasAdmin/editar.html",context)

def eliminarPracticas(request,id):
    practicas=Practicas.objects.get(id=id)
    practicas.estado=False 
    practicas.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaPracticasAdmin")

#CRUD para Jurados

def listarJurado(request): 
    queryset=request.GET.get("buscar")
    jurado=Jurado.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(jurado,7)
        jurado=paginator.page(page)
    except:
        raise Http404
    if queryset:
         jurado=Jurado.objects.filter( 
             Q(jurado__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':jurado,
                'paginator':paginator}
    return render(request,"juradoAdmin/lista.html",context)


def agregarJurado(request): 
    form=JuradoForm()
    if request.method=="POST": 
        form=JuradoForm(request.POST,files=request.FILES)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaJurado")
    else:
        form=JuradoForm()
    context={'form':form}
    return render(request,"juradoAdmin/agregar.html",context)


def editarJurado(request,id): 
    jurado=Jurado.objects.get(id=id)
    if request.method=="POST":
        form=JuradoForm(request.POST,files=request.FILES,instance=jurado) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaJurado")
    else:
        form=JuradoForm(instance=jurado)
    
    context={"form":form}
    return render(request,"juradoAdmin/editar.html",context)

def eliminarJurado(request,id):
    jurado=Jurado.objects.get(id=id)
    jurado.estado=False 
    jurado.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaJurado")

#CRUD para Linea de Investigación

def listarLineaInv(request): 
    queryset=request.GET.get("buscar")
    lineaInv=LineaInvestigacion.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(lineaInv,7)
        lineaInv=paginator.page(page)
    except:
        raise Http404
    if queryset:
         lineaInv=LineaInvestigacion.objects.filter( 
             Q(lineaInvestigacion__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':lineaInv,
                'paginator':paginator}
    return render(request,"lineaInvestigacion/lista.html",context)


def agregarLineaInv(request): 
    form=LineaInvestigacionForm()
    if request.method=="POST": 
        form=LineaInvestigacionForm(request.POST)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaLineaInv")
    else:
        form=LineaInvestigacionForm()
    context={'form':form}
    return render(request,"lineaInvestigacion/agregar.html",context)


def editarLineaInv(request,id): 
    lineaInv=LineaInvestigacion.objects.get(id=id)
    if request.method=="POST":
        form=LineaInvestigacionForm(request.POST,instance=lineaInv) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaLineaInv")
    else:
        form=LineaInvestigacionForm(instance=lineaInv)
    
    context={"form":form}
    return render(request,"lineaInvestigacion/editar.html",context)

def eliminarLineaInv(request,id):
    lineaInv=LineaInvestigacion.objects.get(id=id)
    lineaInv.estado=False 
    lineaInv.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaLineaInv")


#CRUD PARA ASESOR DE TESIS


def listarAsesorTesis(request): 
    queryset=request.GET.get("buscar")
    asesorTesis=AsesorTesis.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(asesorTesis,7)
        asesorTesis=paginator.page(page)
    except:
        raise Http404
    if queryset:
         asesorTesis=AsesorTesis.objects.filter( 
             Q(asesorTesis__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':asesorTesis,
                'paginator':paginator}
    return render(request,"asesorTesisAdmin/lista.html",context)


def agregarAsesorTesis(request): 
    form=AsesorTesisForm()
    if request.method=="POST": 
        form=AsesorTesisForm(request.POST)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaAsesorTesis")
    else:
        form=AsesorTesisForm()
    context={'form':form}
    return render(request,"asesorTesisAdmin/agregar.html",context)


def editarAsesorTesis(request,id): 
    asesorTesis=AsesorTesis.objects.get(id=id)
    if request.method=="POST":
        form=AsesorTesisForm(request.POST,instance=asesorTesis) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaAsesorTesis")
    else:
        form=AsesorTesisForm(instance=asesorTesis)
    
    context={"form":form}
    return render(request,"asesorTesisAdmin/editar.html",context)

def eliminarAsesorTesis(request,id):
    asesorTesis=AsesorTesis.objects.get(id=id)
    asesorTesis.estado=False 
    asesorTesis.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaAsesorTesis")

#Funciones CRUD para TESIS

def listarTesisAdmin(request): 
    queryset=request.GET.get("buscar")
    tesis=Tesis.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(tesis,7)
        tesis=paginator.page(page)
    except:
        raise Http404
    if queryset:
         tesis=Tesis.objects.filter( 
             Q(nombreTesis__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':tesis,
                'paginator':paginator}
    return render(request,"tesisAdmin/lista.html",context)


def agregarTesisAdmin(request): 
    form=TesisForm()
    if request.method=="POST": 
        form=TesisForm(request.POST,files=request.FILES)
        if form.is_valid():
         form.estado=True 
         form.save()
         messages.success(request,"Guardado correctamente")
         return redirect("listaTesisAdmin")
    else:
        form=TesisForm()
    context={'form':form}
    return render(request,"tesisAdmin/agregar.html",context)


def editarTesisAdmin(request,id): 
    tesis=Tesis.objects.get(id=id)
    if request.method=="POST":
        form=TesisForm(request.POST,instance=tesis,files=request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request,"Actualizado correctamente")
            return redirect("listaTesisAdmin")
    else:
        form=TesisForm(instance=tesis)
    
    context={"form":form}
    return render(request,"tesisAdmin/editar.html",context)

def eliminarTesisAdmin(request,id):
    tesis=Tesis.objects.get(id=id)
    tesis.estado=False 
    tesis.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaTesisAdmin")

# CRUD USUARIOS Y ROLES

from SeguridadApp.models import Perfil
from adminApp.forms import SignUpForm1
from django.contrib.auth.models import User

#CRUD para PERFIL

def listarPerfil(request): 
    queryset=request.GET.get("buscar")
    perfil=Perfil.objects.filter(estado=True) 
    page=request.GET.get("page", 1)
    try: 
        paginator=Paginator(perfil,7)
        perfil=paginator.page(page)
    except:
        raise Http404
    if queryset:
         perfil=Perfil.objects.filter( 
             Q(rol__icontains=queryset),estado=True 
             ).distinct()
    context={'entity':perfil,
                'paginator':paginator}
    return render(request,"perfil/lista.html",context)


def agregarPerfil(request): 
    
    model=Perfil
    form=SignUpForm1()
    if request.method=="POST": 
        form=SignUpForm1(request.POST)
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
                
                    messages.success(request,"Usuario Guardado correctamente")
                return redirect("listaPerfil")

            if perf == "alumno":
                carrera=Carrera.objects.get(id = 1)
                alumno = Alumno(nombres= form.cleaned_data.get('first_name'),apellidos= form.cleaned_data.get('last_name'),
                correoUnitru= form.cleaned_data.get('email'),celular= "987654321",carreras = carrera)
               
                alumno.save()
                if usuario is not None:
                    messages.success(request,"Usuario Guardado correctamente")
                return redirect("listaPerfil")

            if perf == "administrador":
                
                admin=User.objects.get(username = form.cleaned_data.get('username'))
                admin.is_superuser =True
                admin.save()

                if usuario is not None:
                    messages.success(request,"Usuario Guardado correctamente")
                return redirect("listaPerfil")
                
            
                   
    context={'form':form}
    return render(request,"perfil/agregar.html",context)


def editarPerfil(request,id): 
    usuario=User.objects.get(id=id)
    if request.method=="POST":
        form=SignUpForm1(request.POST,instance=usuario) 
        if form.is_valid():
            form.save()
            usuario0 = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario1=User.objects.get(username=usuario0)
            perfil=Perfil.objects.get(usuario=usuario1)
            perfil.rol=form.cleaned_data.get('rol')
            perfil.save()

            perf=form.cleaned_data.get('rol')
            if perf == "administrador":
                
                admin=User.objects.get(username = form.cleaned_data.get('username'))
                admin.is_superuser =True
                admin.save()
            else: 
                admin=User.objects.get(username = form.cleaned_data.get('username'))
                admin.is_superuser =False
                admin.save()

            messages.success(request,"Actualizado correctamente")
            return redirect("listaPerfil")
            
    else:
        form=SignUpForm1(instance=usuario)
    
    context={"form":form}
    return render(request,"perfil/editar.html",context)

def eliminarPerfil(request,id):
    perfil=Perfil.objects.get(id=id)
    perfil.estado=False 
    perfil.save()
    messages.success(request,"Eliminado correctamente")
    return redirect("listaPerfil")

#CRUD PARA ROLES

#usuario

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
