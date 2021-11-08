from django.urls import path

from .views import AlunoCreate, ContatoCreate, CursosCreate, EestadualCreate, EnderecoCreate, InscricaoCreate, \
    CursoDelete, InscricaoList, InscricaoUpdate
from .views import AlunoUpdate, ContatoUpdate, EestadualUpdate, EnderecoUpdate, CursosUpdate
from .views import AlunoDelete, AlunoList, ContatoList, EnderecoList, EscolaList, CursosList

app_name = "cadastros"

urlpatterns = [
    # Para criar url de uma view usamos as três declarações:
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
    path('cadastrar/aluno', AlunoCreate.as_view(), name='cadastrar-aluno'),
    path('cadastrar/contato', ContatoCreate.as_view(), name='cadastrar-contato'),
    path('cadastrar/cursos', CursosCreate.as_view(), name='cadastrar-cursos'),
    path('cadastrar/escola', EestadualCreate.as_view(), name='cadastrar-escola'),
    path('cadastrar/endereco', EnderecoCreate.as_view(), name='cadastrar-endereco'),
    path('cadastrar/inscricao', InscricaoCreate.as_view(), name='cadastrar-inscricao'),

    path('editar/aluno/', AlunoUpdate.as_view(), name='editar-aluno'),
    path('editar/contato/', ContatoUpdate.as_view(), name='editar-contato'),
    path('editar/escola/', EestadualUpdate.as_view(), name='editar-escola'),
    path('editar/endereco/', EnderecoUpdate.as_view(), name='editar-endereco'),
    path('editar/curso', CursosUpdate.as_view(), name='editar-curso'),
    path('editar/inscricao', InscricaoUpdate.as_view(), name='editar-inscricao'),

    path('excluir/aluno/', AlunoDelete.as_view(), name='excluir-aluno'),
    path('excluir/curso/', CursoDelete.as_view(), name='excluir-curso'),

    path('listar/aluno/', AlunoList.as_view(), name='listar-aluno'),
    path('listar/contato/', ContatoList.as_view(), name='listar-contato'),
    path('listar/endereco/', EnderecoList.as_view(), name='listar-endereco'),
    path('listar/escola/', EscolaList.as_view(), name='listar-escola'),
    path('listar/cursos/', CursosList.as_view(), name='listar-cursos'),
    path('listar/inscricao/', InscricaoList.as_view(), name='listar-inscricao'),

]
