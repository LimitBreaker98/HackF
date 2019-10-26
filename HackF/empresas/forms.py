from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = [
            'nombre',
            'email',
            'telefono',
            'ubicacion',
        ]

        labels = {
            'nombre' : 'Nombre',
            'email': 'E-Mail',
            'telefono': 'Teléfono',
            'ubicacion': 'Ubicación',
        }