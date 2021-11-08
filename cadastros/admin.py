from django.contrib import admin

# Importar as Classes criadas em Models:

from .models import Aluno, Contato, Cursos, Eestadual, Endereco, Inscricao

# Registrar as Classes aqui:

admin.site.register(Aluno)
admin.site.register(Contato)
admin.site.register(Cursos)
admin.site.register(Eestadual)
admin.site.register(Endereco)
admin.site.register(Inscricao)
