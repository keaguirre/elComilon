"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path

#---importando home
from front.views import backhome

#FROM back
from back.views import login
#from back.views import registro1
from back.views import perfil
from back.views import validarusuario
from back.views import carro
from back.views import registro
from back.views import convenios
from back.views import cerrar_sesion
from back.views import pagina_logout
from back.views import registrarUsuario
from back.views import registrado
from back.views import administracion
#from back.views import eliminarUsuario


#---path('Alias',NombreFuncion en views)
urlpatterns = [
    #Panel administrador
    path('admin/', admin.site.urls),

    #path para volver a home desde seccion
    path('',backhome, name='backhome'),

    #importando las secciones
    path('registro',registro),
    path('login',login),
    path('perfil',perfil),
    path('carro',carro),
    path('convenios',convenios),

    
    #Te lleva a perfil si es exitosa si no a login
    path('validarusuario',validarusuario),
    
    #Cierra sesion
    path('cerrar_sesion', cerrar_sesion),

    #pagina post-cierre sesion
    path('logout', pagina_logout),

    #funcion registro de usuario
    path('registrarUsuario', registrarUsuario),
    
    #pagina post-registrado
    path('registrado', registrado),

    #pagina administracion
    path('administracion', administracion),

    #funcion eliminar usuario logeado
#   path('eliminarUsuario', eliminarUsuario),
]
