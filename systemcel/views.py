# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.


class PaginaInicial(TemplateView):
    template_name = "systemcel/base.html"


# def index(request):
  #  return HttpResponse("Página Inicial do C.E.L 'Prof. Estevam Ferri'")


# def cadastrar_aluno(request):
  #  return render(request, "cadastro.html")


