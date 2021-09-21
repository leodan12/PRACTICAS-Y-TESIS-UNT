from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import EmailField
from django.utils import tree
# Create your models here.

class Facultad(models.Model):
    facultad=models.CharField('Facultad',max_length=60) 
    estado=models.BooleanField(default=True)

    def  __str__(self):
        return self.facultad


class Carrera(models.Model):
    carrera=models.CharField('Carrera',max_length=60) 
    facultad=models.ForeignKey(Facultad,on_delete=models.CASCADE)
    estado=models.BooleanField(default=True)


    def  __str__(self):
        return self.carrera


class Alumno(models.Model):
    nombres=models.CharField('Nombres',max_length=60)
    apellidos=models.CharField('Apellidos',max_length=60)
    correoUnitru=models.EmailField('Correo unitru')
    celular=models.CharField('Celular',max_length=15)
    carreras=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    estado=models.BooleanField(default=True)
    
    def  __str__(self):
        return self.apellidos

class AsesorPracticas(models.Model):
    asesorPracticas=models.CharField('Asesor de Prácticas',max_length=60)
    estado=models.BooleanField(default=True)
    
    def  __str__(self):
        return self.asesorPracticas

#Relacion muchos a muchos
class Practicas(models.Model):
    horasPractica=models.IntegerField('Horas')
    lugarPractica=models.CharField('Lugar',max_length=90)
    fechaInicio=models.DateField('Fecha inicio')
    fechaFinal=models.DateField('Fecha final')
    porcentajeAvance=models.CharField('Porcentaje de Avance',max_length=30, null=True)
    informePracticas=models.FileField(upload_to='practicas/pdfs/',null=True)
    estadoPractica=models.CharField("Estado",max_length=20,default="Revisión")
    asesorPracticas=models.ForeignKey(AsesorPracticas,on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,null=True)
    estado=models.BooleanField(default=True)

    def  __str__(self):
        return self.lugarPractica

class AsesorTesis(models.Model):
    asesorTesis=models.CharField('Asesor de Tesis',max_length=60)
    estado=models.BooleanField(default=True)
    
    def  __str__(self):
        return self.asesorTesis

class Jurado(models.Model):
    jurado=models.CharField('Jurado',max_length=60)
    estado=models.BooleanField(default=True)
    
    def  __str__(self):
        return self.jurado
        
class LineaInvestigacion(models.Model):
    lineaInvestigacion=models.CharField('Línea de Investigación',max_length=60)
    estado=models.BooleanField(default=True)
     
    def  __str__(self):
        return self.lineaInvestigacion

#Relacion muchos a muchos
class Tesis(models.Model):
    nombreTesis=models.CharField("Nombre de Tesis",max_length=60,null=True)
    lineaInvestigacion=models.ForeignKey(LineaInvestigacion,on_delete=models.CASCADE,null=True)
    fechaInicio=models.DateField('Fecha inicio')
    fechaFinal=models.DateField('Fecha final')
    planTesis=models.FileField(upload_to="tesis/pdfs",null=True)
    informeFinal=models.FileField(upload_to="tesis/pdfs", null=True)
    estadoTesis=models.CharField("Estado",max_length=20,default="Revisión")
    asesorTesis=models.ForeignKey(AsesorTesis,on_delete=models.CASCADE)
    jurado=models.ForeignKey(Jurado,on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno,on_delete=models.CASCADE,null=True)
    estado=models.BooleanField(default=True)

    def  __str__(self):
        return self.estadoTesis


        
