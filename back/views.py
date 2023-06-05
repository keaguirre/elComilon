from http.client import HTTPResponse
from django.contrib.auth import logout
from urllib import response
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .models import Usuario
from .models import Producto
from .models import Pedido
# Create your views here.

#-------------------------Funciones de LOGIN y VALIDACION de usuario-------------------------
def login(request):
    return render(request, 'login.html')

def carro(request):
    return render(request,'carro.html')

def registro(request):
    return render(request,'registro.html')

#si el usuario no esta ingresado, te manda al login
def convenios(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    else:
        return render(request, 'convenios.html')


#Recibimos los datos del formulario via POST
def validarusuario(request):
    v_correo = request.POST.get('loginEmail')
    v_pass = request.POST.get('loginPassword')
    try:
    #Buscamos el usuario en la base de datos
        usu=Usuario.objects.get(email=v_correo, password=v_pass)

        if usu:
            request.session['usuario'] = v_correo
            return redirect('/perfil')

    except:
        return redirect('/login')
#Esta funcion evita entrar a perfil directo
def perfil(request):
    if 'usuario' not in request.session:
        return redirect('/login')
    else:
        return render(request, 'perfil.html')

def pagina_logout(request):
    return render(request,'logout.html')

#pagina de administracion
def administracion(request):
    return render(request,'administracion.html')

#funcion cerrar sesion
def cerrar_sesion(request):
    if 'usuario' in request.session:
        logout(request)
        return redirect('/logout')
    else:
        return redirect('/logout')

#--------------Registro de data BBDD-------------------
#funcion post-registro
def registrado(request):
    return render(request,'registrado.html')

def registrarUsuario(request):
    r_correo = request.POST.get('mailRegistro')
    r_nombre = request.POST.get('nombreRegistro')
    r_pass = request.POST.get('passwordRegistro')
#----------parche: editar para que busque el usuario creado y asi comprobar el registro del usuario
    r_User = Usuario(email=r_correo, nombre=r_nombre, password=r_pass)
    r_User.save()
    return redirect('/registrado')

'''def eliminarUsuario(request):
    if  'usuario' in request.session:
        'usuario'.delete()
        logout(request)
        return redirect ('/logout')
    else:
        error_msj = "Ha habido un problema para eliminar el usuario"
        return HttpResponse(error_msj)'''
