from django import forms
 
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido", max_length=50)
    materia_cursada= forms.CharField (label="Materia cursada", max_length=50)

class TutoresFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    apellido = forms.CharField(label="Apellido", max_length=50)
    materia_dictada =forms.CharField(label="Materia dictada", max_length=50)

class NotasFormulario(forms.Form):
    estudiante= forms.CharField(label="Nombre del estudiante", max_length=100)
    materia=forms.CharField(label="Materia", max_length=50)
    nota=forms.IntegerField(label="Nota")