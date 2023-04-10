from django.urls import path
from gallery.views import index, imagem


urlpatterns = [
    path('', index),
    path('imagem/', imagem)
]