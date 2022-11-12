from datetime import datetime
import email
from pyexpat import model
from django.db import models
from django.forms import EmailField

# Create your models here.
 
class Clientes_model (models.Model):
     
     MUJER = 'Femenino'
     HOMBRE = 'Masculino'
     OTRO = 'Otro'
     GENEROS = [
          (MUJER,'Mujer'),
          (HOMBRE,'Hombre'),
          (OTRO,'Otro'),
                ]
     
     id= models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=50, blank = True, null = True)
     apellido = models.CharField(max_length=50)
     dni= models.IntegerField(blank = True, null = True)
     fecha_nac = models.DateField(auto_now_add=False,auto_now=False,null=True)
     edad = models.IntegerField() 
     Generos = models.CharField(max_length=20,
                                choices = GENEROS,
                                default = MUJER)
     
     telefono = models.IntegerField()
     telefono_emergencia = models.IntegerField()
     email = models.EmailField(max_length=50)
     red_social = models.CharField(max_length=50)
     
     def __str__(self)-> str:
          return self.nombre +" "+ self.apellido 
     
     def save(self,commit=True):
          objecto1=super().save(commit=commit)
          
class Salud_model(models.Model):
     SI = 'Si'
     NO = 'No'
     
     OPCIONES= [
          (SI,'Si'),
          (NO,'No'),
                ]
     pregunta_1= models.CharField(max_length=3,
                                  choices=OPCIONES,
                                  default = NO)
     pregunta_2= models.CharField(max_length=3,
                                  choices=OPCIONES,
                                  default = NO)
     pregunta_3= models.CharField(max_length=3,
                                  choices=OPCIONES,
                                  default = NO)
     
     
      
class FichaTec_model(models.Model): 
     persona = models.ForeignKey(Clientes_model, on_delete=models.CASCADE)
     owner = models.IntegerField('Dueño datos',blank = True, default= 1)
     dni= models.IntegerField(blank = True, null = True)
     peso = models.FloatField(blank = True, null = True)
     altura = models.FloatField(blank = True, null = True)
     pregunta_1 = models.CharField(max_length=50,blank = True, null = True)
     pregunta_2 = models.CharField(max_length=50,blank = True, null = True)
     pregunta_3 = models.CharField(max_length=50,blank = True, null = True)
     
     
     def __str__(self)-> str:
          return self.persona 
     
     
class Pagis_model(models.Model):
     fecha_inicio= models.DateField()
     modo_de_pago=models.CharField(max_length=20, blank=False)
     plan = models.CharField(max_length=20, blank=False)  
     fecha_vencimiento=models.DateField()
     dias_de_entrenamiento=models.IntegerField()
     
     
    