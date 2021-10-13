from django.urls import path

from .views import AlunoCreate, ContatoCreate, CursosCreate, EestadualCreate, EnderecoCreate

app_name = "cadastros"

urlpatterns = [
    # Para criar url de uma view usamos as três declarações:
    # path('endereço/', MinhaView.as_view(), name='nome-da-url'),
    path('cadastrar/aluno', AlunoCreate.as_view(), name='cadastrar-aluno'),
    path('cadastrar/contato', ContatoCreate.as_view(), name='cadastrar-contato'),
    path('cadastrar/cursos', CursosCreate.as_view(), name='cadastrar-cursos'),
    path('cadastrar/escola', EestadualCreate.as_view(), name='cadastrar-escola'),
    path('cadastrar/endereco', EnderecoCreate.as_view(), name='cadastrar-endereco'),

]
