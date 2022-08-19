"""appweb URL Configuration

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
from django.contrib import admin
from django.urls import path
from asignaturas.views import buscarAsignatura, editarAsignatura, eliminarAsignatura, registrarAsignatura
from clases.views import buscarClase, editarClase, eliminarClase, registrarClase
from estudiantes.views import index, registrarEstudiante, eliminarEstudiante, buscarEstudiante, editarEstudiante
from profesores.views import buscarProfesor, editarProfesor, eliminarProfesor, registrarProfesor


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),  # index

    # Estudiante
    path('registrar-estudiante/', registrarEstudiante),
    path('buscar-estudiante/<id>', buscarEstudiante),
    path('estudiante/<id>', editarEstudiante),
    path('eliminar-estudiante/<id>/', eliminarEstudiante),

    # Profesores
    path('registrar-profesor/', registrarProfesor),
    path('buscar-profesor/<id>', buscarProfesor),
    path('profesor/<id>', editarProfesor),
    path('eliminar-profesor/<id>/', eliminarProfesor),


    # Asignatura
    path('registrar-asignatura/', registrarAsignatura),
    path('buscar-asignatura/<id>', buscarAsignatura),
    path('asignatura/<id>', editarAsignatura),
    path('eliminar-asignatura/<id>/', eliminarAsignatura),

    # Clases
    path('registrar-clase/', registrarClase),
    path('buscar-clase/<id>', buscarClase),
    path('clase/<id>', editarClase),
    path('eliminar-clase/<id>/', eliminarClase),


]
