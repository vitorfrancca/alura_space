from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from galery.models import Fotografia


def index(request):

    fotografias = Fotografia.objects.order_by("date_photo").filter(published= True)

    return render(request, 'galery/index.html', {"cards": fotografias})


def imagem(request, foto_id):

    fotografia = get_object_or_404(Fotografia, pk=foto_id)

    return render(request, 'galery/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("date_photo").filter(published= True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET ['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(name__icontains= nome_a_buscar)

    return render(request, "galery/buscar.html", {"cards": fotografias})
