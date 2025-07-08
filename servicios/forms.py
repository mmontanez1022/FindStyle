from django import forms
from .models import Servicios

class ServiciosForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ['title', 'description','imagen', 'precio'] 
        widgets ={
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe un titulo'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe una descripción'}),
            
        }