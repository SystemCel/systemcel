from django.views.generic.edit import CreateView

from .models import Aluno, Contato, Cursos, Eestadual, Endereco

from django.urls import reverse_lazy

# Create your views here.


class AlunoCreate(CreateView):
    model = Aluno
    fields = ['cpf', 'p_nome', 'sobrenome', 'dt_nasc',
     'numero_rg', 'numero_ra', 'nome_mae', 'sexo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class ContatoCreate(CreateView):
    model = Contato
    fields = ['tel_aluno', 'tel_mae', 'tel_pai', 'tel_recado', 
    'num_whatsapp', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class CursosCreate(CreateView):
    model = Cursos
    fields = ['nome', 'dia_semana', 'horario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class EestadualCreate(CreateView):
    model = Eestadual
    fields = ['nome', 'serie', 'nivel']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')


class EnderecoCreate(CreateView):
    model = Endereco
    fields = ['logradouro', 'nome', 'numero', 'cep', 'bairro', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('index')
