from django.contrib import admin
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('objetivos/', views.objetivos, name="objetivos"),
    path('noticias/', views.noticias, name="noticias"),
    path('proyectos/', views.proyectos, name="proyectos"),
    path('listado/', views.listado, name="listado"),
    path('post/', views.post, name="post"),
    path('inicioSesion/', views.inicioSesion, name="inicioSesion"),
    path('registrarse/', views.registrarse, name="registrarse"),
    path('contacto/', views.contacto, name="contacto"),
    path('admin/', admin.site.urls),
]






