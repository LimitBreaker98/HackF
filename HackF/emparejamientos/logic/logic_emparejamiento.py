from ..models import Emparejamiento
from ofertas.models import Oferta
from productos.models import Producto
from ofertas.logic.logic_oferta import get_productos_oferta
from campesinos.models import Campesino

def get_emparejamientos():
  queryset = Oferta.objects.all()[:10]
  return (queryset)

def create_emparejamientos(form):
  emparejamiento = form.save()
  emparejamiento.save()
  return ()

def get_top_emparejamientos_for_producto(producto_id):
  producto = Producto.objects.get(id = producto_id)
  lista_ofertas = []
  todas_ofertas = list(Oferta.objects.all())
  print(todas_ofertas)
  while (len(lista_ofertas) < 3):
    mejor_oferta = None
    puntaje = -100
    for oferta in todas_ofertas:
      res = matching(oferta, producto)
      if matching(oferta, producto) > puntaje and res > 0 and oferta not in lista_ofertas:
        puntaje = matching(oferta, producto)
        mejor_oferta = oferta
    lista_ofertas.append(mejor_oferta)
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
  variable = 1
  if producto not in get_productos_oferta(oferta.pk):
    variable = 0

  #Todo: Mejorar formula

  return variable