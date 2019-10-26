
from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
  class Meta:
    model = Producto
    fields =[
      'nombre',
      'descripcion',
      'precio',
      'ubicacion',
      'unidad_medida',
      'tipo',
      'fecha'
    ]

    labels = {
      'nombre': 'Nombre',
      'descripcion': 'Descripción',
      'precio': 'Precio',
      'ubicacion': 'Ubicación',
      'unidad_medida': 'Unidad de medida',
      'tipo': 'Tipo de producto',
      'fecha': 'Fecha'
    }