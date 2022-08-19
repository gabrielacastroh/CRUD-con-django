from django.shortcuts import render, redirect
from clases.models import Clase
from estudiantes.models import Estudiante
from asignaturas.models import Asignatura
# Create your views here.


def registrarClase(request):
    data = {}
    asignatura = Asignatura.objects.all()
    estudiante = Estudiante.objects.all()
    clase = Clase.objects.all()
    if request.method == 'POST':
        clases = Clase()
        id_estudiante = request.POST.get('estudiante')
        id_asignatura = request.POST.get('asignatura')

        clases.estudiante_id = id_estudiante
        clases.asignatura_id = id_asignatura
        clases.save()
    data = {'asignatura': asignatura, 'estudiante': estudiante, 'clase': clase}
    return render(request, 'registrarClase.html', data)


def buscarClase(request, id):
    data = {}
    clase = Clase.objects.get(id=id)
    estudiante = Estudiante.objects.all()
    asignatura = Asignatura.objects.all()
    data = {'asignatura': asignatura, 'estudiante': estudiante, 'clase': clase}
    return render(request, 'editarClase.html', data)

def editarClase(request, id):
    if request.method == 'POST':
        clases = Clase()
        id_estudiante = request.POST.get('estudiante')
        id_asignatura = request.POST.get('asignatura')
        clases = Clase.objects.get(id=id)

        clases.estudiante_id = id_estudiante
        clases.asignatura_id = id_asignatura
        clases.save()
    return redirect('/registrar-clase/')


def eliminarClase(request, id):
    clases = Clase.objects.get(id=id)
    clases.delete()
    clase = Clase.objects.all()
    data = {'clase': clase}
    return redirect('/registrar-clase')
