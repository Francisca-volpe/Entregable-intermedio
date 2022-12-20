
from django.urls import path
from App.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("tutores/", tutores, name="tutores"),
    path("notas", notas, name="notas"),
    path("FormularioEstudiantes/", form_estudiantes, name = "Formulario_estudiantes"),
    path("FormularioTutores/", form_tutores, name = "Formulario_tutores"),
    path("FormularioNotas/", form_notas, name = "Formulario_notas"),
    
]