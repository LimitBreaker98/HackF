from django.http import HttpResponse


def index(request):
    return HttpResponse("Estamos en el índice de campesinos.")