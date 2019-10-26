from ..models import Producto

def get_productos():
  queryset = Producto.objects.all().order_by('-creation_date')[:10]
  return (queryset)

def create_producto(form):
  producto = form.save()
  producto.save()
  return ()