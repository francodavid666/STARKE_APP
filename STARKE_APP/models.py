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
     barrio = models.CharField(max_length=50, blank = True, null = True)
     nombre = models.CharField(max_length=50, blank = True, null = True)
     apellido = models.CharField(max_length=50, null = True)
     dni= models.IntegerField(blank = True, null = True)
     fecha_nac = models.DateField(auto_now_add=False,auto_now=False,null=True, blank = True)
     edad = models.IntegerField(blank = True, null = True)
     Generos = models.CharField(max_length=20,
                                choices = GENEROS,
                                default = MUJER,
                                blank = True, null = True)
     
     telefono = models.IntegerField(blank = True, null = True)
     telefono_emergencia = models.IntegerField(blank = True, null = True)
     email = models.EmailField(max_length=50,blank = True, null = True)
     red_social = models.CharField(max_length=50,blank = True, null = True)
     
     def __str__(self)-> str:
          return self.nombre +" "+ self.apellido 
   
          

      
class FichaTec_model(Clientes_model): 
     peso = models.FloatField(blank = True, null = True)
     altura = models.FloatField(blank = True, null = True)
     pregunta_1 = models.CharField(max_length=50,blank = True, null = True)
     pregunta_2 = models.CharField(max_length=50,blank = True, null = True)
     pregunta_3 = models.CharField(max_length=50,blank = True, null = True)
     
      
    
     
class Pagos_model(models.Model):
     fecha_inicio= models.DateField()
     modo_de_pago=models.CharField(max_length=20, blank=False)
     plan = models.CharField(max_length=20, blank=False)  
     fecha_vencimiento=models.DateField()
     dias_de_entrenamiento=models.IntegerField()
     
    
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
     
         
    
     