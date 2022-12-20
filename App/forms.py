from django import forms
 
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    materia = forms.CharField(label="Materia", max_length=50)
    correo = forms.EmailField(label="Correo electrónico")
    

class TutoresFormulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50)
    materia = forms.CharField(label="Materia", max_length=50)
    

class NotasFormulario(forms.Form):
    estudiante= forms.CharField(label="Nombre del estudiante", max_length=100)
    materia=forms.CharField(label="Materia", max_length=50)
    nota=forms.IntegerField(label="Nota")