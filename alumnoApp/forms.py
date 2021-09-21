from django import forms
from django.db.models.fields import CharField
from django.forms import fields, widgets
from adminApp.models import Practicas
from adminApp  .models import Tesis

class PracticasForm(forms.ModelForm):
    #Validaciones
    estadoPractica = (
        
        ('Revision', 'Revision'),
        ('Terminada', 'Terminada'),
        ('Aprobada', 'Aprobada'),)

    estadoPractica = forms.ChoiceField(widget=forms.RadioSelect,choices = estadoPractica,)

    porcentajeAvance=forms.IntegerField()
    horasPractica=forms.IntegerField(min_value=1,max_value=600)
    class Meta:
        model=Practicas
        fields=["horasPractica","lugarPractica","fechaInicio","fechaFinal","asesorPracticas","porcentajeAvance","informePracticas","estadoPractica"]
        labels = { 'fechaInicio': ('Inicio:'), 'fechaFinal': ('Final:'),'horasPractica': ('Horas de prácticas completadas hasta hoy:'),
        'asesorPracticas': ('Asesor de practicas:'),'lugarPractica': ('Lugar de prácticas:'),}

        widgets={
            "fechaInicio": forms.SelectDateWidget(),
            "fechaFinal": forms.SelectDateWidget(),
        }

class TesisForm(forms.ModelForm):

    estadoTesis = (
        
        ('Revision', 'Revision'),
        ('Terminada', 'Terminada'),
        ('Aprobada', 'Aprobada'),)

    estadoTesis = forms.ChoiceField(widget=forms.RadioSelect,choices = estadoTesis,)

    class Meta:
        model=Tesis
        fields=["nombreTesis","lineaInvestigacion","fechaInicio","fechaFinal","asesorTesis","jurado","planTesis","informeFinal","estadoTesis"]
        labels = {'fechaInicio': ('Inicio:'), 'fechaFinal': ('Final:'),'planTesis': ('Plan de tesis:'),
        'asesorTesis': ('Asesor de tesis:'),'informeFinal': ('Informe final:'),'jurado': ('Jurado asignado:'),'estadoTesis': ('Estado de la tesis:'),}
        widgets={
            "fechaInicio": forms.SelectDateWidget(),
            "fechaFinal": forms.SelectDateWidget(),
        }