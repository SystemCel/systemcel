from django.urls import path

from .views import AlunoCreate, ContatoCreate, CursosCreate, EestadualCreate, EnderecoCreate
from .views import AlunoUpdate, ContatoUpdate, EestadualUpdate, EnderecoUpdate
from .views import AlunoDelete


app_name = "cadastros"

urlpatterns = [
    # Para criar url de uma view usamos as três declarações:
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
    path('cadastrar/aluno', AlunoCreate.as_view(), name='cadastrar-aluno'),
    path('cadastrar/contato', ContatoCreate.as_view(), name='cadastrar-contato'),
    path('cadastrar/cursos', CursosCreate.as_view(), name='cadastrar-cursos'),
    path('cadastrar/escola', EestadualCreate.as_view(), name='cadastrar-escola'),
    path('cadastrar/endereco', EnderecoCreate.as_view(), name='cadastrar-endereco'),

    path('editar/aluno/<int:pk>/', AlunoUpdate.as_view(), name='editar-aluno'),
    path('editar/contato/<int:pk>/', ContatoUpdate.as_view(), name='editar-contato'),
    path('editar/escola/<int:pk>/', EestadualUpdate.as_view(), name='editar-escola'),
    path('editar/endereco/<int:pk>/', EnderecoUpdate.as_view(), name='editar-endereco'),

    path('excluir/aluno/<int:pk>/', AlunoDelete.as_view(), name='excluir-aluno'),

]
