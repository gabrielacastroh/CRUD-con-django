from django.contrib import admin
from profesores.models import Profesor
# Register your models here.


class ProfesorAdmin (admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'numIdentificacion',
                    'correo')
    list_filter = ('nombre', 'apellido', 'numIdentificacion')
    search_fields = ('numIdentificacion',)


admin.site.register(Profesor, ProfesorAdmin)
