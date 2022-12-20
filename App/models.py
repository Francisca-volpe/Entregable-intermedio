from django.db import models

class Estudiantes (models.Model):
    nombre=models.CharField(max_length=50)
    materia=models.CharField(max_length=50)
    correo=models.EmailField()
    

class Tutores (models.Model):
    nombre=models.CharField(max_length=50)
    materia=models.CharField(max_length=50)

class Notas (models.Model):
    estudiante=models.CharField(max_length=100)
    materia=models.CharField(max_length=50)
    nota=models.IntegerField()
