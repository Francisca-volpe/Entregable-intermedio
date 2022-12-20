from django.shortcuts import render
from .models import *
import datetime
from django.http import HttpResponse
from django.template import Template, loader, Context
from App.forms import *

def inicio (request):
    dia=datetime.datetime.today()
    return render (request, "App/inicio.html")

def estudiantes (request):
    return render (request, "App/estudiantes.html")

def tutores (request):
    return render (request, "App/tutores.html")

def notas (request):
    return render (request, "App/notas.html")

def form_estudiantes (request):
    if request.method=="POST":
        form=EstudiantesFormulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            materia_cursada=info["materia_cursada"]
            estudiante=Estudiantes(nombre=nombre, apellido=apellido, materia_cursada=materia_cursada)
            estudiante.save()
            return render (request, "App/inicio.html", {"mensaje": "Datos guardados correctamente."})

        else: 
            return render (request, "App/EstudiantesForm.html", {"mensaje": "Datos inválidos"})

    else:
        formulario=EstudiantesFormulario()
        return render (request, "App/EstudiantesForm.html", {"form":formulario})

def form_tutores (request):
    if request.method=="POST":
        form=TutoresFormulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            materia_dictada =info["materia_dictada"]
            tutor=Tutores(nombre=nombre, apellido=apellido, materia_dictada=materia_dictada)
            tutor.save()
            return render (request, "App/inicio.html", {"mensaje": "Datos guardados correctamente."})

        else: 
            return render (request, "App/TutoresForm.html", {"mensaje": "Datos inválidos"})

    else:
        formulario=TutoresFormulario()
        return render (request, "App/TutoresForm.html", {"form":formulario})

def form_notas (request):
    if request.method=="POST":
        form=NotasFormulario(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            estudiante=info["estudiante"]
            materia=info["materia"]
            nota =info["nota"]
            nota=Notas(estudiante=estudiante, materia=materia, nota=nota)
            nota.save()
            return render (request, "App/inicio.html", {"mensaje": "Datos guardados correctamente."})

        else: 
            return render (request, "App/NotasForm.html", {"mensaje": "Datos inválidos"})

    else:
        formulario=TutoresFormulario()
        return render (request, "App/NotasForm.html", {"form":formulario})