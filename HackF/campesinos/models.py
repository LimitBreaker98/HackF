from django.db import models

# Create your models here.

class Campesino(models.Model):
    #productos = ???
    nombre = models.CharField(max_length = 200)
    ubicacion = models.CharField(max_length = 200)

    def __str__(self):
        return self.nombre