from django.shortcuts import render, redirect
from profesores.models import Profesor
# Create your views here.

def registrarProfesor(request):
    data = {}
    profesor = Profesor.objects.all()
    if request.method == 'POST':
        profesores = Profesor()
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        documento = request.POST.get('documento')
        correo = request.POST.get('correo')

        profesores.nombre = nombre
        profesores.apellido = apellido
        profesores.numIdentificacion = documento
        profesores.correo = correo
        profesores.save()
    data = {'profesor': profesor}
    return render(request, 'registrarProfesor.html', data)


def buscarProfesor(request, id):
    data = {}
    profesor = Profesor.objects.get(id=id)
    data = {'profesor': profesor}
    return render(request, 'editarProfesor.html', data)


def editarProfesor(request, id):
    if request.method == 'POST':
        profesores = Profesor()
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        documento = request.POST.get('documento')
        correo = request.POST.get('correo')
        profesores = Profesor.objects.get(id=id)
        profesores.nombre = nombre
        profesores.apellido = apellido
        profesores.numIdentificacion = documento
        profesores.correo = correo
        profesores.save()
    return redirect('/registrar-profesor/')


def eliminarProfesor(request, id):
    profesores = Profesor.objects.get(id=id)
    profesores.delete()
    profesor = Profesor.objects.all()
    data = {'profesores': profesor}
    return redirect('/registrar-profesor/')
