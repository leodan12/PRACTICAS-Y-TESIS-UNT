from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True,label=' Nombres ')
    last_name = forms.CharField(max_length=140, required=True,label=' Apellidos ')
    email = forms.EmailField(required=True)
   
    
    roles = (
        
        ('alumno', 'alumno'),
        ('asesor', 'asesor'),
       
        )

    rol = forms.ChoiceField(widget=forms.RadioSelect,choices = roles,label = 'Rol del Usuario : alumno / asesor ')
    #widget=forms.RadioSelect
    #lo quitamos de rol para que quede como combobox
    class Meta:
        model = User
        fields = [ "username" ,"email","first_name","last_name","password1","password2","rol"] 

     
