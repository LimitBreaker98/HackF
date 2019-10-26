from django.db import models

# Create your models here.
class Producto(models.Model):
  nombre = models.CharField(max_length=100)
  descripcion = models.CharField(max_length=250)
  precio = models.FloatField(default=0.0)
  ubicacion = models.CharField(max_length=250)
  unidad_medida = models.CharField(max_length=50)
  tipo = models.CharField(max_length=250)
  fecha = models.DateTimeField('creation_date')
  
