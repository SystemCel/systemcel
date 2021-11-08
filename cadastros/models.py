from django.db import models
from django.contrib.auth.models import User
from cpf_field.models import CPFField


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


class Aluno(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das Opções"]
    ]

    cpf = CPFField(unique=True, verbose_name="CPF (Somente Números):")
    p_nome = models.CharField(max_length=45, verbose_name="Primeiro Nome")
    sobrenome = models.CharField(max_length=100)
    dt_nasc = models.DateField(verbose_name="Data de Nascimento")
    numero_rg = models.CharField(max_length=9, blank=True, null=True, verbose_name="Número do RG")
    numero_ra = models.CharField(max_length=14, verbose_name="Número do RA")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return "{} ({} {})".format(self.cpf, self.p_nome, self.sobrenome)

    class Meta:
        managed = False
        db_table = 'aluno'
        verbose_name_plural = 'alunos'


class Contato(models.Model):
    tel_aluno = models.CharField(max_length=11, blank=True, null=True, verbose_name="Telefone do Aluno")
    tel_mae = models.CharField(max_length=11, blank=True, null=True, verbose_name="Telefone da Mãe")
    tel_pai = models.CharField(max_length=11, blank=True, null=True, verbose_name="Telefone do Pai")
    tel_recado = models.CharField(max_length=11, blank=True, null=True, verbose_name="Telefone Recado")
    num_whatsapp = models.CharField(max_length=11, blank=True, null=True, verbose_name="Número Whatsapp")
    email = models.CharField(max_length=70)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'contato'
        verbose_name_plural = 'contatos'


class Cursos(models.Model):
    id_cursos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, verbose_name="Nome do Curso")
    turma = models.CharField(unique=True, max_length=3, verbose_name="Turma")
    dia_semana = models.CharField(max_length=45, verbose_name="Dia da Semana")
    horario = models.CharField(max_length=25, verbose_name="Horário")

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'cursos'
        verbose_name_plural = 'cursos'


class Eestadual(models.Model):
    NIVEL_CHOICES = [
        ["Fundamental II", "Fundamental II"],
        ["Médio", "Médio"],
        ["EJA", "EJA"]
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome da Escola")
    serie = models.CharField(max_length=2, verbose_name="Série")
    nivel = models.CharField(max_length=15, verbose_name="Nível", choices=NIVEL_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'eestadual'
        verbose_name_plural = 'escolas'


class Endereco(models.Model):
    LOGRADOURO_CHOICES = [
        ["Alameda", "Alameda"], ["Avenida", "Avenida"], ["Chácara", "Chácara"], ["Estrada", "Estrada"],
        ["Praça", "Praça"], ["Recanto", "Recanto"], ["Rua", "Rua"], ["Sítio", "Sítio"], ["Viela", "Viela"]
    ]
    logradouro = models.CharField(max_length=15, choices=LOGRADOURO_CHOICES)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, verbose_name="Número")
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'endereco'
        verbose_name_plural = 'enderecos'


class Inscricao(models.Model):
    CURSOS_CHOICES = [
        ["Alemão", "Alemão"], ["Espanhol", "Espanhol"], ["Francês", "Francês"], ["Inglês", "Inglês"],
        ["Italiano", "Italiano"], ["Japonês", "Japonês"]
    ]

    DIASEMANA_CHOICES = [
        ["Terça e Quinta", "Alemão - Terça e Quinta"], ["Segunda e Quarta", "Espanhol - Segunda e Quarta"],
        ["Terça e Quinta", "Espanhol - Terça e Quinta"], ["Terça e Quinta", "Francês - Terça e Quinta"],
        ["Terça e Quinta", "Italiano - Terça e Quinta"], ["Segunda e Quarta", "Inglês - Segunda e Quarta"],
        ["Terça e Quinta", "Inglês - Terça e Quinta"], ["Segunda e Quarta", "Japonês - Segunda e Quarta"]
    ]
    HORARIO_CHOICES = [
        ["17:10 às 18:50", "Alemão 3ª e 5ª- 17:10 às 18:50"], ["08:00 às 09:40", "Espanhol 2ª e 4ª- 08:00 às 09:40"],
        ["17:10 às 18:50", "Espanhol 2ª e 4ª- 17:10 às 18:50"], ["19:10 às 20:50", "Espanhol 2ª e 4ª- 19:10 às 20:50"],
        ["15:30 às 17:10", "Espanhol 3ª e 5ª- 15:30 às 17:10"], ["17:10 às 18:50", "Espanhol 3ª e 5ª- 17:10 às 18:50"],
        ["08:00 às 09:40", "Francês 3ª e 5ª- 08:00 às 09:40"], ["19:10 às 20:50", "Francês 3ª e 5ª- 19:10 às 20:50"],
        ["13:30 às 15:10", "Italiano 3ª e 5ª- 13:30 às 15:10"], ["17:10 às 18:50", "Inglês 2ª e 4ª- 17:10 às 18:50"],
        ["19:10 às 20:50", "Inglês 2ª e 4ª- 19:10 às 20:50"], ["09:40 às 11:20", "Inglês 3ª e 5ª- 09:40 às 11:20"],
        ["15:30 às 17:10", "Inglês 3ª e 5ª- 15:30 às 17:10"], ["17:10 às 18:50", "Inglês 3ª e 5ª- 17:10 às 18:50"],
        ["17:10 às 18:50", "Japonês 2ª e 4ª- 17:10 às 18:50"]
    ]
    # Field name made lowercase.
    aluno_cpf = models.CharField(
        db_column='Aluno_cpf', primary_key=True, max_length=11)
    curso1 = models.CharField(max_length=45, verbose_name="Nome do Curso 1", choices=CURSOS_CHOICES)
    turma1 = models.CharField(max_length=3, null=True, verbose_name="Turma")
    dia_semana1 = models.CharField(max_length=45, verbose_name="Dia da Semana", choices=DIASEMANA_CHOICES)
    horario1 = models.CharField(max_length=25, verbose_name="Horário", choices=HORARIO_CHOICES)
    curso2 = models.CharField(max_length=45, blank=True, null=True, verbose_name="Nome do Curso 2",
                              choices=CURSOS_CHOICES)
    turma2 = models.CharField(max_length=3, blank=True, null=True, verbose_name="Turma")
    dia_semana2 = models.CharField(max_length=45, blank=True, null=True, verbose_name="Dia da Semana",
                                   choices=DIASEMANA_CHOICES)
    horario2 = models.CharField(max_length=25, blank=True, null=True, verbose_name="Horário", choices=HORARIO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "{} -> {} | {} a {}".format(self.curso1, self.turma1, self.dia_semana1, self.horario1,
                                           self.curso2, self.turma2, self.dia_semana2, self.horario2)

    class Meta:
        managed = False
        db_table = 'inscricao'
        verbose_name_plural = 'inscricoes'
