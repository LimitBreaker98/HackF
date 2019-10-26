from ..models import Campesino

def get_campesinos():
  queryset = Campesino.objects.all()[:10]
  return (queryset)

def create_campesino(form):
  producto = form.save()
  producto.save()
  return ()
  