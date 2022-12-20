from django.db import models

from django.db import models

class Estudiantes (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    materias=models.CharField(max_length=100)

class Tutores (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    correp=models.EmailField()

class Notas (models.Model):
    estudiante=models.CharField(max_length=100)
    materia=models.CharField(max_length=50)
    nota=models.IntegerField()
