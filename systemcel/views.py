
# Importar o TemplateView para criar páginas simples.
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = "systemcel/index.html"


class SobreView(TemplateView):
  template_name = "systemcel/sobre.html"

