from django import forms
from django.db.models.fields import CharField
from django.forms import fields, widgets
from django.forms.models import ALL_FIELDS
from adminApp.models import Alumno, Practicas,AsesorPracticas,AsesorTesis,Carrera,Facultad,Jurado,LineaInvestigacion,Tesis
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from SeguridadApp.models import Perfil

class SignUpForm1(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True,label=' Nombres ')
    last_name = forms.CharField(max_length=140, required=True,label=' Apellidos ')
    email = forms.EmailField(required=True)
   
    
    roles = (
        
        ('alumno', 'alumno'),
        ('asesor', 'asesor'),
        ('administrador', 'administrador'),
        )

    rol = forms.ChoiceField(widget=forms.RadioSelect,choices = roles,label = 'Rol del Usuario : alumno / asesor ')
    #widget=forms.RadioSelect
    #lo quitamos de rol para que quede como combobox
    class Meta:
        model = User
        fields = [ "username" ,"email","first_name","last_name","password1","password2","rol" ,] 


class FacultadForm(forms.ModelForm):
    class Meta:
        model=Facultad
        fields= '__all__'

class CarreraForm(forms.ModelForm):
    class Meta:
        model=Carrera
        fields='__all__'

class AlumnoForm(forms.ModelForm):
    class Meta:
        model=Alumno
        fields='__all__'

class AsesorPracticasForm(forms.ModelForm):
    class Meta:
        model=AsesorPracticas
        fields='__all__'

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
        fields="__all__"
        labels = { 'fechaInicio': ('Inicio:'), 'fechaFinal': ('Final:'),'horasPractica': ('Horas de prácticas completadas hasta hoy:'),
        'asesorPracticas': ('Asesor de practicas:'),'lugarPractica': ('Lugar de prácticas:'),}

        widgets={
            "fechaInicio": forms.SelectDateWidget(),
            "fechaFinal": forms.SelectDateWidget(),
        }

class AsesorTesisForm(forms.ModelForm):
    class Meta:
        model=AsesorTesis
        fields='__all__'

class JuradoForm(forms.ModelForm):
    class Meta:
        model=Jurado
        fields='__all__'

class LineaInvestigacionForm(forms.ModelForm):
    class Meta:
        model=LineaInvestigacion
        fields='__all__'

class TesisForm(forms.ModelForm):

    estadoTesis = (
        
        ('Revision', 'Revision'),
        ('Terminada', 'Terminada'),
        ('Aprobada', 'Aprobada'),)

    estadoTesis = forms.ChoiceField(widget=forms.RadioSelect,choices = estadoTesis,)

    class Meta:
        model=Tesis
        fields='__all__'
        labels = {'fechaInicio': ('Inicio:'), 'fechaFinal': ('Final:'),'planTesis': ('Plan de tesis:'),
        'asesorTesis': ('Asesor de tesis:'),'informeFinal': ('Informe final:'),'jurado': ('Jurado asignado:'),'estadoTesis': ('Estado de la tesis:'),}
        widgets={
            "fechaInicio": forms.SelectDateWidget(),
            "fechaFinal": forms.SelectDateWidget(),
        }