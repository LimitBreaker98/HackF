from django.db import models
from campesinos.models import Campesino
from empresas.models import Empresa

# Create your models here.
class Emparejamiento(models.Model):
  razones = models.CharField(max_length=100)
  campesino = models.OneToOneField(Campesino, on_delete = models.CASCADE, null = True, blank = True)
  empresa = models.OneToOneField(Empresa, on_delete = models.CASCADE, null = True, blank = True)
  telefono = models.CharField(max_length=100)
  ubicacion = models.CharField(max_length=100)
  favorabilidad = models.FloatField() #Favorabilidad entre 0 y 1.


  def __str__(self):
    return "Un match con un {}% entre el {} y {} ha sido encontrado: \n Las razones son:{}". format(favorabilidad * 100, campesino, empresa, razones);