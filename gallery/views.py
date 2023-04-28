from django.shortcuts import render


data = {
    1: {'nome': 'Nebulosa de Carina',
        'legenda': 'webbtelescope.org / NASA / James Webb'}, 
    2: {'nome': 'Galáxia NGC 1079',
        'legenda': 'nasa.org / NASA / Hubble'}
}

def index(request):
    return render(request, 'gallery/index.html')

def imagem(request):
    return render(request, 'gallery/imagem.html')