from django.db import models
from campesinos.models import Campesino
from empresas.models import Empresa

# Create your models here.

class Oferta(models.Model):
    #productos = ???
    fecha_entrega = models.CharField(max_length = 200)
    ubicacion_entrega = models.CharField(max_length = 200)
    estado = models.CharField(max_length = 20)
    minorista = models.ForeignKey(Empresa, on_delete = models.CASCADE, null = True) 
    campesino = models.ForeignKey(Campesino, on_delete = models.CASCADE, null = True)
    