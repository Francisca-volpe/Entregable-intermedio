from django.shortcuts import render

from django.shortcuts import render
from .models import *
import datetime
from django.http import HttpResponse

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
    return render (request, "EntregableApp/form_estudiantes.html")
