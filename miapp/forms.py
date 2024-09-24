
from django import forms
from.models import tareas

class taskform(forms.ModelForm):
    class Meta:
        model=tareas
        fields=['nombre','descripcion']
        widgets={
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de la tarea'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control','placeholder':'Descripcion de la tarea'})
        }

