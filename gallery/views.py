from django.shortcuts import render


def index(request):
    
    data = {
    1: {'nome': 'Nebulosa de Carina',
        'legenda': 'webbtelescope.org / NASA / James Webb'}, 
    2: {'nome': 'Galáxia NGC 1079',
        'legenda': 'nasa.org / NASA / Hubble'}
    }

    return render(request, 'gallery/index.html', {'cards': data})

def imagem(request):
    return render(request, 'gallery/imagem.html')