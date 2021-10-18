from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Aluno, Contato, Cursos, Eestadual, Endereco

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.


class AlunoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aluno
    fields = ['cpf', 'p_nome', 'sobrenome', 'dt_nasc',
              'numero_rg', 'numero_ra', 'nome_mae', 'sexo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_context_data(self, *args, **kwargs):
        context = super(AlunoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro Pessoal de Aluno:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(AlunoCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class ContatoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Contato
    fields = ['tel_aluno', 'tel_mae', 'tel_pai', 'tel_recado',
              'num_whatsapp', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_context_data(self, *args, **kwargs):
        context = super(ContatoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Contatos:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(ContatoCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class CursosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Cursos
    fields = ['nome', 'dia_semana', 'horario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_context_data(self, *args, **kwargs):
        context = super(CursosCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Cursos:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(CursosCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class EestadualCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Eestadual
    fields = ['nome', 'serie', 'nivel']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_context_data(self, *args, **kwargs):
        context = super(EestadualCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Escola Estadual:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(EestadualCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class EnderecoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['logradouro', 'nome', 'numero', 'cep', 'bairro', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_context_data(self, *args, **kwargs):
        context = super(EnderecoCreate, self).get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Endereço do Aluno:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(EnderecoCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url
