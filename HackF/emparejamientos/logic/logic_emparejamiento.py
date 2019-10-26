from ..models import Emparejamiento
from ofertas.models import Oferta


def get_emparejamientos():
  queryset = Emparejamiento.objects.all()[:10]
  return (queryset)

def create_emparejamientos(form):
  emparejamiento = form.save()
  emparejamiento.save()
  return ()

def get_top_emparejamientos_for_producto(producto):
  lista_ofertas = []
  todas_ofertas = list(Oferta.objects.all())
  while (len(lista_ofertas < 3)):
    mejor_oferta = None
    puntaje = -100
    for oferta in todas_ofertas:
      if matching(oferta, producto) > mejor_oferta:
        puntaje = matching(oferta, producto)
        mejor_oferta = oferta
    lista_ofertas.append(mejor_oferta)
    todas_ofertas.remove(mejor_oferta)
  return lista_ofertas


def matching(oferta, producto):
  #fecha_entrega
  #ubicacion entrega
  #estado
  #campesino
  #minorista

  #nombre
  #descripcion
  #precio
  #ubicacion
  #unidad_medida
  #tipo
  #fecha
  #campesino
  #oferta

  return oferta.abs(oferta.fecha_entrega - producto.fecha)