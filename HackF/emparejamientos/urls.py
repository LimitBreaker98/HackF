from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('top_offers/<int:pk>', views.get_top_3_offers, name='top_3_matching')
]