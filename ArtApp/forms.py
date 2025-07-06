from django import forms
from .models import SolicitudComision

class SolicitudComisionForm(forms.ModelForm):
    class Meta:
        model = SolicitudComision
        fields = ['nombre', 'email', 'tipo', 'descripcion', 'referencias']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'tu@email.com'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe tu solicitud de comisión...'
            }),
            'referencias': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://ejemplo.com/referencia'
            })
        }
        labels = {
            'nombre': 'Nombre completo',
            'email': 'Correo electrónico',
            'tipo': 'Tipo de comisión',
            'descripcion': 'Descripción',
            'referencias': 'URL de referencias (opcional)'
        }
