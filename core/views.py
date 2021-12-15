from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("Home")

def objetivos(request):
    return HttpResponse("objetivos")

def noticias(request):
    return HttpResponse("Noticias")

def proyectos(request):
    return HttpResponse("Proyectos")

def listado(request):
    return HttpResponse("listado de busqueda")

def post(request):
    return HttpResponse("Post")

def inicioSesion(request):
    return HttpResponse("iniciar sesion")

def registrarse(request):
    return HttpResponse("registrarse")

def contacto(request):
    return HttpResponse("Contacto")