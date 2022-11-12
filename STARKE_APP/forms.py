
from django import forms
from .models import *
from django.forms import ModelForm
from django.conf import settings
from django.forms.widgets import NumberInput




class Clientes_form(forms.ModelForm):
  
  fecha_nac= forms.DateField(widget=forms.DateInput(attrs={'placeholder':'Dia-Mes-Año'},format = '%d/%m/%Y'), input_formats=settings.DATE_INPUT_FORMATS)    
  class Meta: 
         model= Clientes_model
         fields= '__all__'
         widgets = {'nombre':forms.TextInput(
           attrs={'class':'form-control','placeholder':'Nombre','color':'red',}),
         
         'apellido':forms.TextInput(
           attrs={'class':'forms-control','placeholder':'Apellido',}
         ),
         'edad':forms.TextInput(
           attrs={'class':'forms-control','placeholder':'edad'}
         ),
          'telefono':forms.TextInput(
           attrs={'class':'forms-control','placeholder':'1166709006'}
         ),
           'telefono_emergencia':forms.TextInput(
           attrs={'class':'forms-control','placeholder':'1166709006'}
         ),
            'email':forms.TextInput(
           attrs={'class':'forms-control','placeholder':'Email'}
         ),
             'red_social':forms.TextInput(
           attrs={'class':'forms-control','placeholder':'link de red social'}
         ),
         }
  
  
  
class fichaTec_form(forms.ModelForm):
  
  class Meta:
    model = FichaTec_model
    fields ='__all__'