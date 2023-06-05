from django.shortcuts import render

# Create your views here.
def homedehome(request):#home desde home
    return render(request,'index.html')

def backhome(request):#volver a home desde secciones
    return render(request,'index.html')

# views modelos

# views funciones | urls
