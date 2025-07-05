from django import forms
from .models import Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['title', 'description', 'important', 'imagen'] 
        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe un titulo'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripción'}),
            'important' : forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),
        }