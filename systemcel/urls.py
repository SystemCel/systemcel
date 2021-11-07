# from django.conf.urls import url
from django import urls
# from django.contrib import admin
from django.urls import path
from .views import InglesView, PaginaInicial, SobreView, GaleriaView
from .views import AlemaoView, EspanholView, FrancesView, ItalianoView
from .views import JaponesView, MandarimView

# from . import views

app_name = "systemcel"

urlpatterns = [
    # Para criar url de uma view usamos as três declarações:
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),

    path('', PaginaInicial.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('ingles/', InglesView.as_view(), name='ingles'),
    path('italiano/', ItalianoView.as_view(), name='italiano'),
    path('alemao/', AlemaoView.as_view(), name='alemao'),
    path('espanhol/', EspanholView.as_view(), name='espanhol'),
    path('frances/', FrancesView.as_view(), name='frances'),
    path('japones/', JaponesView.as_view(), name='japones'),
    path('mandarim/', MandarimView.as_view(), name='mandarim'),
    path('galeria/', GaleriaView.as_view(), name='galeria'),

]
