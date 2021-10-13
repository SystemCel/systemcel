# from django.conf.urls import url
from django import urls
# from django.contrib import admin
from django.urls import path
from .views import PaginaInicial, SobreView

# from . import views

app_name = "systemcel"

urlpatterns = [
    # Para criar url de uma view usamos as três declarações:
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
    
    path('', PaginaInicial.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    
]
