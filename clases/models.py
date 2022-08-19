from django.db import models
from asignaturas.models import Asignatura
from estudiantes.models import Estudiante

# Create your models here.


class Clase (models.Model):
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, null=True, blank=True)
    asignatura = models.ForeignKey(
        Asignatura, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.estudiante+" "+self.asignatura
