from django.db import models

# Create your models here.

class Solicitud(models.Model):
    #productos = ???
    fecha_entrega = models.CharField(max_length = 200)
    productos = models.CharField(max_length = 200)
    ubicacion_entrega = models.CharField(max_length = 200)
    empresa = models.ForeignKey('Campesino')

    
    def __str__(self):
        return self.nombre