from braces.views import GroupRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Aluno, Contato, Cursos, Eestadual, Endereco, Inscricao

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404


# Create your views here.

# ############## CLASSES CREATE ##################


class AlunoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aluno
    fields = ['cpf', 'p_nome', 'sobrenome', 'dt_nasc',
              'numero_rg', 'numero_ra', 'nome_mae', 'sexo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:cadastrar-endereco')

    def get_context_data(self, *args, **kwargs):
        context = super(AlunoCreate, self).get_context_data(**kwargs)

        context['titulo'] = "Dados Pessoais do Aluno:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem salvo no banco de dados!
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
    success_url = reverse_lazy('cadastros:cadastrar-escola')

    def get_context_data(self, *args, **kwargs):
        context = super(ContatoCreate, self).get_context_data(**kwargs)

        context['titulo'] = "Dados de Contatos do Aluno:"
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
    fields = ['nome', 'turma', 'dia_semana', 'horario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:cadastrar-cursos')

    def get_context_data(self, *args, **kwargs):
        context = super(CursosCreate, self).get_context_data(**kwargs)

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
    success_url = reverse_lazy('cadastros:editar-inscricao')

    def get_context_data(self, *args, **kwargs):
        context = super(EestadualCreate, self).get_context_data(**kwargs)

        context['titulo'] = "Dados da Escola Atual do Aluno:"
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
    success_url = reverse_lazy('cadastros:cadastrar-contato')

    def get_context_data(self, *args, **kwargs):
        context = super(EnderecoCreate, self).get_context_data(**kwargs)

        context['titulo'] = "Cadastro de Endereço do Aluno:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem salvo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(EnderecoCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class InscricaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Inscricao
    fields = ['aluno_cpf', 'curso1', 'dia_semana1', 'horario1',
              'curso2', 'dia_semana2', 'horario2']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:listar-inscricao')

    def get_context_data(self, **kwargs):
        context = super(InscricaoCreate, self).get_context_data(**kwargs)

        context['titulo'] = "Escolha seus Cursos:"
        context['botao'] = "Cadastrar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem salvo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(InscricaoCreate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


# ############## CLASSES UPDATE ##################


class AlunoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Aluno
    fields = ['cpf', 'p_nome', 'sobrenome', 'dt_nasc',
              'numero_rg', 'numero_ra', 'nome_mae', 'sexo']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super(AlunoUpdate, self).get_context_data(**kwargs)

        context['titulo'] = "Editar Dados Pessoais do Aluno:"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem salvo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(AlunoUpdate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class ContatoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Contato
    fields = ['tel_aluno', 'tel_mae', 'tel_pai', 'tel_recado',
              'num_whatsapp', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super(ContatoUpdate, self).get_context_data(**kwargs)

        context['titulo'] = "Editar Dados de Contatos do Aluno:"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(ContatoUpdate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class EestadualUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Eestadual
    fields = ['nome', 'serie', 'nivel']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super(EestadualUpdate, self).get_context_data(**kwargs)

        context['titulo'] = "Editar Dados da Escola Atual do Aluno:"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(EestadualUpdate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class EnderecoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Endereco
    fields = ['logradouro', 'nome', 'numero', 'cep', 'bairro', 'cidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super(EnderecoUpdate, self).get_context_data(**kwargs)

        context['titulo'] = "Editar Endereço do Aluno:"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(EnderecoUpdate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class CursosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Cursos
    fields = ['nome', 'turma', 'dia_semana', 'horario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:cadastrar-cursos')

    def get_context_data(self, *args, **kwargs):
        context = super(CursosUpdate, self).get_context_data(**kwargs)

        context['titulo'] = "Atualização de Cursos:"
        context['botao'] = "Atualizar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem slavo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(CursosUpdate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


class InscricaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Inscricao
    fields = ['aluno_cpf', 'curso1', 'dia_semana1', 'horario1',
              'curso2', 'dia_semana2', 'horario2']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('cadastros:listar-inscricao')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, usuario=self.request.user)
        return self.object

    def get_context_data(self, **kwargs):
        context = super(InscricaoUpdate, self).get_context_data(**kwargs)

        context['titulo'] = "Modifique seus Cursos:"
        context['botao'] = "Editar"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'

        return context

    def form_valid(self, form):
        # Antes do Super o Objeto não foi criado e nem salvo no banco de dados!
        form.instance.usuario = self.request.user

        url = super(InscricaoUpdate, self).form_valid(form)

        # Depois do Super o Objeto está criado!

        return url


# ############## CLASSES DELETE ##################


class AlunoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Aluno
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('systemcel:inicio')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Aluno, usuario=self.request.user)
        return self.object


class CursoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cursos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('cadastros:listar-cursos')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Cursos, usuario=self.request.user)
        return self.object


# ############## CLASSES LISTVIEW ##################


class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'cadastros/listar/aluno.html'

    def get_queryset(self):
        self.object_list = Aluno.objects.filter(usuario=self.request.user)
        return self.object_list


class ContatoList(LoginRequiredMixin, ListView):
    model = Contato
    template_name = 'cadastros/listar/contato.html'

    def get_queryset(self):
        self.object_list = Contato.objects.filter(usuario=self.request.user)
        return self.object_list


class EnderecoList(LoginRequiredMixin, ListView):
    model = Endereco
    template_name = 'cadastros/listar/endereco.html'

    def get_queryset(self):
        self.object_list = Endereco.objects.filter(usuario=self.request.user)
        return self.object_list


class EscolaList(LoginRequiredMixin, ListView):
    model = Eestadual
    template_name = 'cadastros/listar/escola.html'

    def get_queryset(self):
        self.object_list = Eestadual.objects.filter(usuario=self.request.user)
        return self.object_list


class CursosList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    group_required = u"admin"
    model = Cursos
    template_name = 'cadastros/listar/cursos.html'


class InscricaoList(LoginRequiredMixin, ListView):
    model = Inscricao
    template_name = 'cadastros/listar/inscricao.html'

    def get_queryset(self):
        self.object_list = Inscricao.objects.filter(usuario=self.request.user)
        return self.object_list

