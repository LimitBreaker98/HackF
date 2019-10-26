from ..models import Campesino

def get_campesinos():
  queryset = Campesino.objects.all()[:10]
  return (queryset)

def create_campesino(form):
  producto = form.save()
  producto.save()
  return ()

def get_campesino_by_name(name):
  return Campesino.objects.get(nombre = name)
  