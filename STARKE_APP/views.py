from django.shortcuts import render,redirect
from django.http import HttpResponse
from STARKE_APP.forms import *
from .models import *
from django.db.models import Q
from django.contrib import messages



# Create your views here.

def inicio(request):
    return render (request,"STARKE_APP/inicio.html")

def login (request):
    return render (request, "STARKE_APP/login.html")

def usuario_creado (request):
    return render (request, "STARKE_APP/get.html")







def formulario_login(request):
    
    if request.method == "POST":
        formulario = Clientes_form(request.POST)
        
        if formulario.is_valid():
            info= formulario.cleaned_data
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            mail = info.get("mail")
            edad = info.get("edad")
            
            persona_1 = Clientes_model(nombre=nombre, apellido=apellido, mail=mail , edad=edad)
            persona_1.save()
            
            return render (request, "STARKE_APP/usuario_creado.html")
        else:
            return render(request,"STARKE_APP/inicio.html" )
    else:
        formulario = Clientes_form()
    return render(request,"STARKE_APP/formulario_login.html",{"formulario_p": formulario_persona})    
    
    
    
    # Clientes
    
def clientes (request):
    queryset = request.GET.get('buscar')
    print(queryset)
    form = Clientes_model.objects.filter(nombre = True)
    if queryset:
        form = Clientes_model.objects.filter(
            Q(nombre__icontains=queryset) |
            Q(apellido__icontains=queryset)
        ).distinct()
        return render (request,'STARKE_APP/clientes/clientes.html',{'form':form})

    return render (request,'STARKE_APP/clientes/buscar_cliente.html',{'form':form})



def add_cliente (request):
       
    if request.method == "POST":
        formulario = Clientes_form(request.POST)
        
        if formulario.is_valid():
            info= formulario.cleaned_data
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            dni = info.get("dni")
            fecha_nac = info.get("fecha_nac")
            email = info.get("email")
            edad = info.get("edad")
            Generos = info.get("Generos")
            telefono = info.get("telefono")
            telefono_emergencia = info.get("telefono_emergencia")
            red_social = info.get("red_social")
            
            persona_1 = Clientes_model(nombre=nombre,
                                       apellido=apellido,
                                       dni=dni,
                                       fecha_nac=fecha_nac,
                                       email=email,
                                       edad=edad,
                                       Generos=Generos,
                                       telefono=telefono,
                                       telefono_emergencia=telefono_emergencia,
                                       red_social=red_social)
            persona_1.save()
            return render(request,"STARKE_APP/inicio.html" )
        else: 
         messages.info(request,'Algo salio mal')
         return redirect ('add_cliente')
    else:
        form = Clientes_form()
    return render(request,"STARKE_APP/clientes/add_cliente.html",{'form': form})    

    

def detalle_cliente (request, id):
    
    form= Clientes_model.objects.filter(id=id)
    form_2= FichaTec_model.objects.all()
    return render (request, 'STARKE_APP/clientes/detalle_cliente.html',{'form':form,'form_2':form_2})


 
def modificar_datos_personales(request,id):
    cliente= Clientes_model.objects.get(id=id)
    if request.method =='POST':
        
        form = Clientes_form(request.POST)
        if form.is_valid():
            
            info = form.cleaned_data
            cliente.nombre=info['nombre']
            cliente.apellido=info['apellido']
            cliente.dni=info['dni']
            cliente.fecha_nac=info['fecha_nac']
            cliente.edad=info['edad']
            cliente.Generos=info['Generos']
            cliente.telefono=info['telefono']
            cliente.telefono_emergencia=info['telefono_emergencia']
            cliente.email=info['email']
            cliente.red_social=info['red_social']
            
            cliente.save()
            return redirect('inicio')
        else:
            messages.info(request,'Algo salio mal')
            return redirect ('modificar_datos_personales')
    form = Clientes_form(initial={'nombre':cliente.nombre,
                                  'apellido':cliente.apellido,
                                  'fecha_nac':cliente.fecha_nac,
                                  'edad':cliente.edad,
                                  'dni':cliente.dni,
                                  'Genero':cliente.Generos,
                                  'telefono':cliente.telefono,
                                  'telefono_emergencia':cliente.telefono_emergencia,
                                  'email':cliente.email,
                                  'red_social':cliente.red_social})
    return render (request,'STARKE_APP/clientes/modificar_datos_personales.html',{'form':form,'id':id})
    
    
    
def eliminar_cliente(request,id):
    clientes=Clientes_model.objects.filter(id=id)
    if len(clientes)!=0:
        cliente=clientes[0]
        cliente.delete()
        
    return redirect('inicio')    
     
        
   
def ficha_tecnica (request,id):
 if request.method =='POST':
     cliente=Clientes_model.get(id=id)
     formulario = fichaTec_form(request.POST)
     formulario2 = Clientes_form(request.POST)
     
     if formulario.is_valid():
         
         info2=formulario2.cleaned_data
         info=formulario.cleaned_data
         
         cliente.id = info['id']
         
         persona=info.get("persona")
         peso = info.get("peso")
         dni=info.get("dni")
         altura = info.get("altura")
         pregunta_1 = info.get("pregunta_1")
         pregunta_2 = info.get("pregunta_2")
         pregunta_3 = info.get("pregunta_3")
        
         ficha_1 = FichaTec_model(persona=persona,
                                  peso=peso,
                                    altura=altura,
                                    dni=dni,
                                    pregunta_1=pregunta_1,
                                    pregunta_2=pregunta_2,
                                    pregunta_3=pregunta_3)    
    
         ficha_1.save()
         return redirect('inicio')
     else:
         messages.info(request,'Algo salio mal')
         return redirect('ficha_tecnica')
 
 form = fichaTec_form()
 formulario2=Clientes_form(initial={'dni':cliente.id})
 form_2=Clientes_model()
 return render (request,'STARKE_APP/clientes/ficha_tecnica.html',{'form':form,'form_2':form_2})
         
    