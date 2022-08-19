from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('registrar-estudiante/', views.registrarEstudiante),
    path('buscar-estudiante/<id>', views.buscarEstudiante),
    path('<id>', views.editarEstudiante),
    path('<id>/', views.eliminarEstudiante),
]
