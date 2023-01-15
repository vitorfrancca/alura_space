from django.shortcuts import render
from django.http import HttpResponse




def index(request):

    dados = {
    1: {"nome": "Nebulosa de Carina"
    ,"legenda": "webbtelescope.org / NASA / James Webb" },
    2: {"nome": "Galaxia NGC 1079",
    "legenda": "nasa.org / NASA / Hubble"}
}
    return render(request, 'galery/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'galery/imagem.html')