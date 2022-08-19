from django.contrib import admin
from estudiantes.models import Estudiante
# Register your models here.


class EstudianteAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numIdentificacion',
                    'correo', 'programaAcademico')
    list_filter = ('nombre', 'apellido', 'numIdentificacion')
    search_fields = ('numIdentificacion', 'programaAcademico')


admin.site.register(Estudiante, EstudianteAdmin)
