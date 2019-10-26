from django.db import models

# Create your models here.
class Empresa(models.Model):
  nombre = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  telefono = models.CharField(max_length=100)
  ubicacion = models.CharField(max_length=100)
