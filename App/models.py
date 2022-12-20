from django.db import models

class Estudiantes (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    materia_cursada=models.CharField(max_length=100)

class Tutores (models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    materia_dictada=models.CharField(max_length=100)

class Notas (models.Model):
    estudiante=models.CharField(max_length=100)
    materia=models.CharField(max_length=50)
    nota=models.IntegerField()
