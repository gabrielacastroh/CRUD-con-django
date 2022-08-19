from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    numIdentificacion = models.CharField(max_length=15)
    correo = models.EmailField(max_length=30)
    programaAcademico = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+" "+self.apellido
