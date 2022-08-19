from django.shortcuts import render, redirect
from asignaturas.models import Asignatura
from profesores.models import Profesor
# Create your views here.


def registrarAsignatura(request):
    data = {}
    asignatura = Asignatura.objects.all()
    profesor = Profesor.objects.all()
    if request.method == 'POST':
        asignaturas = Asignatura()
        nombre = request.POST.get('nombre')
        salon = request.POST.get('salon')
        horario = request.POST.get('horario')
        id_profesor = request.POST.get('profesor')

        asignaturas.nombre = nombre
        asignaturas.salon = salon
        asignaturas.horario = horario
        asignaturas.profesor_id = id_profesor
        asignaturas.save()
    data = {'asignatura': asignatura, 'profesor': profesor}
    return render(request, 'registrarAsignatura.html', data)


def buscarAsignatura(request, id):
    data = {}
    asignatura = Asignatura.objects.get(id=id)
    profesor = Profesor.objects.all()
    data = {'asignatura': asignatura, 'profesor': profesor}
    return render(request, 'editarAsignatura.html', data)


def editarAsignatura(request, id):
    if request.method == 'POST':
        asignaturas = Asignatura()
        nombre = request.POST.get('nombre')
        salon = request.POST.get('salon')
        horario = request.POST.get('horario')
        id_profesor = request.POST.get('profesor')
        asignaturas = Asignatura.objects.get(id=id)

        asignaturas.nombre = nombre
        asignaturas.salon = salon
        asignaturas.horario = horario
        asignaturas.profesor_id = id_profesor
        asignaturas.save()
    return redirect('/registrar-asignatura/')


def eliminarAsignatura(request, id):
    asignaturas = Asignatura.objects.get(id=id)
    asignaturas.delete()
    asignatura = Asignatura.objects.all()
    data = {'asignatura': asignatura}
    return redirect('/registrar-asignatura')
