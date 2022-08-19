from django.db import models
from profesores.models import Profesor
# Create your models here.


class Asignatura (models.Model):
    nombre = models.CharField(max_length=20)
    salon = models.CharField(max_length=10)
    horario = models.CharField(max_length=15)
    profesor = models.ForeignKey(
        Profesor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre+" "+self.salon
