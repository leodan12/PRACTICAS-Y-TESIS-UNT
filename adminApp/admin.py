from django.contrib import admin
from adminApp.models import Alumno,Facultad,Carrera,AsesorPracticas, LineaInvestigacion,Practicas,AsesorTesis,Tesis,Jurado
from SeguridadApp.models import Perfil
# Register your models here.

class FacultadAdmin(admin.ModelAdmin):
    list_display=("facultad","estado")

class CarreraAdmin(admin.ModelAdmin):
    list_display=("carrera","facultad","estado")

class AlumnoAdmin(admin.ModelAdmin):
    list_display=("nombres","apellidos","correoUnitru","celular","estado","carreras")

class AsesorPracticasAdmin(admin.ModelAdmin):
    list_display=("asesorPracticas","estado")

class AsesorTesisAdmin(admin.ModelAdmin):
    list_display=("asesorTesis","estado")

class JuradoAdmin(admin.ModelAdmin):
    list_display=("jurado","estado")

class PracticasAdmin(admin.ModelAdmin):
    list_display=("horasPractica","lugarPractica","fechaInicio","fechaFinal","porcentajeAvance","informePracticas","estadoPractica","asesorPracticas","alumno","estado")

class LineaInvestigacionAdmin(admin.ModelAdmin):
    list_display=('lineaInvestigacion','estado')

class TesisAdmin(admin.ModelAdmin):
    list_display=("nombreTesis","lineaInvestigacion","fechaInicio","fechaFinal","planTesis","informeFinal","estadoTesis","asesorTesis","jurado","alumno","estado")

class PerfilAdmin(admin.ModelAdmin):
    list_display=("usuario","rol")

admin.site.register(Facultad,FacultadAdmin)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(AsesorPracticas,AsesorPracticasAdmin)
admin.site.register(Practicas,PracticasAdmin)
admin.site.register(AsesorTesis,AsesorTesisAdmin)
admin.site.register(Jurado,JuradoAdmin)
admin.site.register(LineaInvestigacion,LineaInvestigacionAdmin)
admin.site.register(Tesis,TesisAdmin)
admin.site.register(Perfil,PerfilAdmin)
