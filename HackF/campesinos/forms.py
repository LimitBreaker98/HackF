from django import forms
from .models import Campesino

class CampesinoForm(forms.ModelForm):
  class Meta:
    model = Campesino
    fields = [
      'nombre',
      'ubicacion',
    ]

    labels = {
        'nombre': 'Nombre',
        'ubicacion': 'Ubicacion'
    }
        