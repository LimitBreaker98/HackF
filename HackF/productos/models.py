from django.db import models
from campesinos.models import Campesino
from ofertas.models import Oferta

# Create your models here.
class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=250)
  precio = models.FloatField(default=0.0)
  ubicacion = models.CharField(max_length=250)
  unidad_medida = models.CharField(max_length=50)
  tipo = models.CharField(max_length=250)
  fecha = models.DateTimeField('creation_date')
  campesino = models.ForeignKey(Campesino, on_delete = models.CASCADE, null = True)
  oferta = models.ForeignKey(Oferta, on_delete = models.CASCADE, null = True)
  