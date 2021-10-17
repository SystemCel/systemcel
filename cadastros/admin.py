from django.contrib import admin

# Importar as Classes criadas em Models:

from .models import Aluno, Contato, Cursos, Eestadual, Endereco

# Registrar as Classes aqui:

admin.site.register(Aluno)
admin.site.register(Contato)
admin.site.register(Cursos)
admin.site.register(Eestadual)
admin.site.register(Endereco)


