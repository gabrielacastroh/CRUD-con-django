from django.contrib import admin
from clases.models import Clase
# Register your models here.


class ClaseAdmin (admin.ModelAdmin):
    list_display = ('estudiante', 'asignatura')
    list_filter = ('estudiante', 'asignatura')
    search_fields = ('estudiante', 'asignatura')


admin.site.register(Clase, ClaseAdmin)
