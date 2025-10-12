import os
from django.contrib  import messages
from django.shortcuts import render
from app_empresaGimnasio.forms import ClienteForm 
from .models import Cliente , Servicio
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
def preuntasFrecu(request):
    return render(request,'app_empresaGimnasio/preguntasFrecuentes.html')

def index(request):
    return render(request,'app_empresaGimnasio/index.html')

def listado(request):
    clientes = Cliente.objects.all()
    return render(request,'app_empresaGimnasio/listadoCliente.html',{'clientes':clientes})

def listadoServicio(request):
    servicios = Servicio.objects.all()
    return render(request,'app_empresaGimnasio/listadoServicio.html',{'servicios':servicios})

def nuevo_cliente(request):
    if request.method =='POST':
        formcliente = ClienteForm(request.POST , request.FILES)
        if formcliente.is_valid():
            formcliente.save()
            messages.success(request,'Cliente creado exitosamente')
            return redirect('listado')
        else:
            messages.error(request,'Atencion : verifique los datos ingresados')
    else:
        formcliente = ClienteForm
    return render(request ,'app_empresaGimnasio/nuevo_cliente.html',{'formcliente':formcliente})

def editar_cliente(request,id):
    cliente = get_object_or_404(Cliente, pk=id)
    formcliente = ClienteForm(instance=cliente)
    if request.method  == 'POST':
        formcliente = ClienteForm(request.POST, request.FILES , instance=cliente)
        if formcliente.is_valid():
            formcliente.save()
            messages.success(request ,'Cliente Editado exitosamente')
            return redirect('listado')
        else:
            messages.success(request,'Atencion : verifique los Datos Ingresados')
    return render (request,'app_empresaGimnasio/editar_cliente.html',{'formcliente':formcliente})

#def eliminar_cliente(request,id):
  #  cliente = get_object_or_404(Cliente , pk=id)
    # Guarda la ruta del archivo del campo imageField antes de eliminar la instancia 
  #  archivo = cliente.imagen.path
    #Elimina la instancia del modelo
    cliente.delete()
    # verifica si el archivo existe y eliminalo
#    if os.path.exists(archivo):
 #      os.remove(archivo)
 #   return redirect('listado')

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    
    # Verifica si el cliente tiene una imagen antes de intentar acceder al archivo
    if cliente.imagen and os.path.exists(cliente.imagen.path):
        # Elimina el archivo si existe
        os.remove(cliente.imagen.path)
    
    # Elimina la instancia del cliente
    cliente.delete()
    
    return redirect('listado')