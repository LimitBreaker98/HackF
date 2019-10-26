from django import forms
from .models import Oferta

class OfertaForm(forms.ModelForm):
    class Meta:
        model = Oferta
        fields = [
            'fecha_entrega',
            'ubicacion_entrega',
            'estado',
            'campesino',
            'minorista'
        ]

        labels = {
            'fecha_entrega': 'Fecha_Entrega',
            'ubicacion_entrega': 'Ubicacion_Entrega',
            'estado': 'Estado',
            'campesino': 'Campesino',
            'minorista': 'Empresa minorista'
        }
        