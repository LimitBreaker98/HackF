from ..models import Emparejamiento
from ofertas.models import Oferta
from ofertas.logic.logic_oferta import get_ofertas
def get_campesinos():
  queryset = Emparejamiento.objects.all()[:10]
  return (queryset)

def create_campesino(form):
  producto = form.save()
  producto.save()
  return ()

def get_top_emparejamientos_for_campesino(campesino):
  lista_ofertas = []
  todas_ofertas = list(get_ofertas())
  while (len(lista_ofertas < 3)):
    mejor_oferta = None
    puntaje = -100
    for oferta in todas_ofertas:
      if 
        
        
        
  return lista_ofertas
  