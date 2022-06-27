from ast import Pass
from cgitb import html
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from AppBanco.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

# Create your views here.

#def inicio(request):
#    if request.user.is_authenticated:
#        print("--------------> User is authenticated")
#    return render(request,'AppBanco/inicio.html')
    #avatar = Avatar.objects.filter(user=request.user)
    #return render(request,'AppBanco/inicio.html' ,{'url':avatar[0].imagen.url})

def inicio(request):

    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user.id)
        if not avatar:
            return render(request,"AppBanco/inicio.html")
        else:
            return render(request,'AppBanco/inicio.html' ,{'url':avatar[0].imagen.url})
    else:
        return render(request,"AppBanco/inicio.html")

def clientes(request):

    if request.method == 'POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Clientes(codigo_cliente=informacion['codigo_cliente'], nombre=informacion['nombre'], email=informacion['email'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=ClienteForm()
    return render(request,"AppBanco/clientes.html",{'formulario':formulario})

def buscar_cliente(request):
    return render(request,"AppBanco/busquedaCliente.html")

def buscar(request):
    if request.GET['codigo_cliente']:
        codigo_cliente=request.GET['codigo_cliente']
        cliente=Clientes.objects.filter(codigo_cliente=codigo_cliente)
        return render(request,"AppBanco/resultadoCliente.html",{'clientes':cliente})    
    else:
        respuesta="No se ingresó ningún código de cliente a buscar"
        return render(request,"AppBanco/resultadoCliente.html",{'respuesta':respuesta})
    
      
def productos(request):
    if request.method == 'POST':
        formulario=ProductoForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Productos(codigo_producto=informacion['codigo_producto'], descripcion=informacion['descripcion'], subproducto=informacion['subproducto'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=ProductoForm()
        return render(request,"AppBanco/productos.html",{'formulario':formulario})

def sucursales(request):
    if request.method == 'POST':
        formulario=SucursalForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Sucursales(codigo_sucursal=informacion['codigo_sucursal'], sucursal=informacion['sucursal'], region=informacion['region'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=SucursalForm()
        return render(request,"AppBanco/sucursales.html",{'formulario':formulario})


def login_view(request):
    if request.method == 'POST':
        formulario=LoginForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            password=formulario.cleaned_data.get('password')
            # Authenticate user      

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # A backend authenticated the credentials    
                print("Login successfuly")            
                # return render(request,"AppBanco/inicio.html")
                return inicio(request)
            else:
                # No backend authenticated the credentials       
                # Return an 'invalid login' error message.
                return render(request,"AppBanco/login.html", {'mensaje':"Usuario o clave inválidas"})

        else:
            return render(request,"AppBanco/inicio.html", {'mensaje':"Formulario Inválido"})

    formulario=LoginForm()
    return render(request, "AppBanco/login.html", {'formulario':formulario})

def register(request):
    if request.method == 'POST':
        formulario=RegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data.get('username')
            formulario.save()
            return render(request,"AppBanco/inicio.html", {'mensaje':"Usuario registrado con éxito"})

    else:
        formulario=RegistrationForm()


    return render(request,"AppBanco/registro.html", {'formulario':formulario})

def logout(request):
    logout(request)
    return render(request,"AppBanco/logout.html")


def leerclientes(request):

    clientes = Clientes.objects.all() #trae todos los clientes
    contexto = {"clientes": clientes}
    return render(request, "AppBanco/leerclientes.html", contexto)


def eliminarclientes(request, cliente_nombre):

    clientes = Clientes.objects.get(nombre=cliente_nombre)
    clientes.delete()

    #vuelvo al menú
    clientes = Clientes.objects.all() #traigo todos los clientes
    contexto = {"clientes":clientes}

    return render(request, "AppBanco/inicio.html",contexto)


def editarcliente(request, cliente_nombre):

      #Recibe el nombre del cliente que vamos a modificar
      clientes = Clientes.objects.get(nombre=cliente_nombre)

      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':

            formulario = ClienteForm(request.POST) 

            print(formulario)

            if formulario.is_valid:   #Si pasó la validación de Django

                  informacion = formulario.cleaned_data

                  clientes.codigo_cliente = informacion['codigo_cliente']
                  clientes.nombre = informacion['nombre']
                  clientes.email = informacion['email']
                  
                  clientes.save()

                  clientess=Clientes.objects.all()
                  contexto={'clientess':clientess}  

                  return render(request, "AppBanco/inicio.html",contexto)  
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            formulario= ClienteForm(initial={'codigo_cliente': clientes.codigo_cliente, 'nombre':clientes.nombre , 
            'email':clientes.email}) 

      #Voy al html que me permite editar
      return render(request, "AppBanco/editarcliente.html", {"formulario":formulario, "cliente_nombre":cliente_nombre})
 

def agregarclientes(request):

    if request.method == 'POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            cliente = Clientes(codigo_cliente=informacion['codigo_cliente'], nombre=informacion['nombre'], email=informacion['email'])
            cliente.save()
            return render(request,"AppBanco/inicio.html")
    else:
        formulario=ClienteForm()
    return render(request,"AppBanco/agregarcliente.html",{'formulario':formulario})


@login_required
def editarperfil(request):

    
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "AppBanco/inicio.html")
    else:
        formulario = UserEditForm(initial={ 'email':usuario.email})

    return render(request, "AppBanco/editarperfil.html", {"formulario":formulario, "usuario":usuario})



def about(request):
    return render(request,"AppBanco/about.html")