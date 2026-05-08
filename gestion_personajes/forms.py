from django import forms
from .models import Clase, Personaje, Raza


class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre', 'descripcion', 'dado_vida']


class PersonajeForm(forms.ModelForm):
    class Meta:
        model = Personaje
        fields = [
            'nombre', 'nivel', 'experiencia',
            'vida_actual', 'vida_maxima',
            'fuerza', 'destreza', 'constitucion',
            'inteligencia', 'sabiduria', 'carisma',
            'user', 'raza', 'clase'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del personaje'}),
            'nivel': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'experiencia': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'vida_actual': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'vida_maxima': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'fuerza': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'destreza': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'constitucion': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'inteligencia': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'sabiduria': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'carisma': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'raza': forms.Select(attrs={'class': 'form-control'}),
            'clase': forms.Select(attrs={'class': 'form-control'}),
        }

class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = ['nombre', 'descripcion', 'bono_fuerza', 'bono_destreza', 
                  'bono_constitucion', 'bono_inteligencia', 'bono_sabiduria', 'bono_carisma']
