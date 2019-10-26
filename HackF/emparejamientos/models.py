from django.db import models
from campesinos.models import Campesino
from empresas.models import Empresa

# Create your models here.
class Emparejamiento(models.Model):
  razones = models.CharField(max_length=100)
  campesino = models.OneToOneField(Campesino, null = True, blank = True)
  empresa = models.OneToOneField(Empresa, null = True, blank = True)
  telefono = models.CharField(max_length=100)
  ubicacion = models.CharField(max_length=100)
  favorabilidad = models.FloatField() #Favorabilidad entre 0 y 1.


  def __str__(self):
    return f"Un match con un {favorabilidad * 100}% entre el {campesino} y {empresa} ha sido encontrado: \n Las razones son:{razones}";