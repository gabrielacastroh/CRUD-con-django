from django.shortcuts import render, redirect
from estudiantes.models import Estudiante
# Create your views here.


def index(request):
    return render(request, 'index.html')


def registrarEstudiante(request):
    data = {}
    estudiante = Estudiante.objects.all()
    if request.method == 'POST':
        estudiantes = Estudiante()
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        documento = request.POST.get('documento')
        progAcademico = request.POST.get('progAcademico')
        correo = request.POST.get('correo')

        estudiantes.nombre = nombre
        estudiantes.apellido = apellido
        estudiantes.numIdentificacion = documento
        estudiantes.correo = correo
        estudiantes.programaAcademico = progAcademico
        estudiantes.save()
    data = {'estudiante': estudiante}
    return render(request, 'registrarEstudiante.html', data)


def buscarEstudiante(request, id):
    data = {}
    estudiante = Estudiante.objects.get(id=id)
    data = {'estudiante': estudiante}
    return render(request, 'editarEstudiante.html', data)


def editarEstudiante(request, id):
    if request.method == 'POST':
        estudiantes = Estudiante()
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        documento = request.POST.get('documento')
        progAcademico = request.POST.get('progAcademico')
        correo = request.POST.get('correo')
        estudiantes = Estudiante.objects.get(id=id)
        estudiantes.nombre = nombre
        estudiantes.apellido = apellido
        estudiantes.numIdentificacion = documento
        estudiantes.correo = correo
        estudiantes.programaAcademico = progAcademico
        estudiantes.save()
    return redirect('/registrar-estudiante/')


def eliminarEstudiante(request, id):
    estudiantes = Estudiante.objects.get(id=id)
    estudiantes.delete()
    estudiante = Estudiante.objects.all()
    data = {'estudiante': estudiante}
    return redirect('/registrar-estudiante')
