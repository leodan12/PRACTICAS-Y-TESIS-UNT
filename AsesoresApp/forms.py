from django import forms
from django.forms import fields
from adminApp.models import Practicas
from adminApp.models import Tesis


class PracticasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PracticasForm, self).__init__(*args, **kwargs)
        # Agregar el atributo 'required' al campo name
        self.fields['alumno'].widget.attrs = {
            'readonly': True ,
            
        }
        self.fields['fechaInicio'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['fechaFinal'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['horasPractica'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['asesorPracticas'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['lugarPractica'].widget.attrs = {
            'readonly': True,
            
        }

    estadoPractica = (
        
        ('Revision', 'Revision'),
        ('Terminada', 'Terminada'),
        ('Aprobada', 'Aprobada'),)

    estadoPractica = forms.ChoiceField(widget=forms.RadioSelect,choices = estadoPractica,)

    porcentajeAvance=forms.IntegerField()

    class Meta:
        model=Practicas
        fields=["alumno","fechaInicio","fechaFinal","horasPractica","asesorPracticas","lugarPractica","porcentajeAvance","estadoPractica","informePracticas"]
        labels = { 'alumno': ('Nombre del Alumno:'),'fechaInicio': ('Inicio:'), 'fechaFinal': ('Final:'),'horasPractica': ('Horas de practicas completadas hasta hoy:'),
        'asesorPracticas': ('Asesor de practicas:'),'lugarPractica': ('Nombre del lugar de practicas:'),}

class TesisForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):
        super(TesisForm, self).__init__(*args, **kwargs)
        # Agregar el atributo 'required' al campo name
        self.fields['alumno'].widget.attrs = {
        'readonly': True ,
            
        }
        self.fields['fechaInicio'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['fechaFinal'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['jurado'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['asesorTesis'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['nombreTesis'].widget.attrs = {
            'readonly': True,
            
        }
        self.fields['lineaInvestigacion'].widget.attrs = {
            'readonly': True,
            
        }

    estadoTesis = (
        
        ('Revision', 'Revision'),
        ('Terminada', 'Terminada'),
        ('Aprobada', 'Aprobada'),)

    estadoTesis = forms.ChoiceField(widget=forms.RadioSelect,choices = estadoTesis,)
    
    class Meta:
        model=Tesis
        fields=["nombreTesis","lineaInvestigacion","alumno","fechaInicio","fechaFinal","asesorTesis","jurado","planTesis","informeFinal","estadoTesis"]
        labels = { 'alumno': ('Nombre del Alumno:'),'fechaInicio': ('Inicio:'), 'fechaFinal': ('Final:'),'planTesis': ('Plan de tesis:'),
        'asesorTesis': ('Asesor de tesis:'),'informeFinal': ('Informe final:'),'jurado': ('Jurado asignado:'),'estadoTesis': ('Estado de la tesis:'),}