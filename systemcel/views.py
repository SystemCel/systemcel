# Importar o TemplateView para criar páginas simples.
from django.views.generic import TemplateView


# Create your views here.

class PaginaInicial(TemplateView):
    template_name = "systemcel/index.html"


class SobreView(TemplateView):
    template_name = "systemcel/sobre.html"


class InglesView(TemplateView):
    template_name = "systemcel/ingles.html"


class AlemaoView(TemplateView):
    template_name = "systemcel/alemao.html"


class EspanholView(TemplateView):
    template_name = "systemcel/espanhol.html"


class FrancesView(TemplateView):
    template_name = "systemcel/frances.html"


class GaleriaView(TemplateView):
    template_name = "systemcel/galeria.html"


class ItalianoView(TemplateView):
    template_name = "systemcel/italiano.html"


class JaponesView(TemplateView):
    template_name = "systemcel/japones.html"


class MandarimView(TemplateView):
    template_name = "systemcel/mandarim.html"

