from django.contrib import admin
from asignaturas.models import Asignatura
# Register your models here.


class AsignaturaAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'salon', 'horario',
                    'profesor')
    list_filter = ('nombre', 'profesor')
    search_fields = ('nombre', 'profesor')


admin.site.register(Asignatura, AsignaturaAdmin)