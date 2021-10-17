from django.db import models
from django.contrib.auth.models import User


class Aluno(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das Opções"]
    ]

    id_aluno = models.AutoField(primary_key=True)
    cpf = models.CharField(unique=True, max_length=14, verbose_name="Número do CPF")
    p_nome = models.CharField(max_length=45, verbose_name="Primeiro Nome")
    sobrenome = models.CharField(max_length=100)
    dt_nasc = models.DateField(verbose_name="Data de Nascimento")
    numero_rg = models.CharField(max_length=9, blank=True, null=True, verbose_name="Número do RG")
    numero_ra = models.CharField(max_length=14, verbose_name="Número do RA")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    id_endereco = models.ForeignKey(
        'Endereco', models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)
    id_contato = models.ForeignKey(
        'Contato', models.DO_NOTHING, db_column='id_contato', blank=True, null=True)
    id_eestadual = models.ForeignKey(
        'Eestadual', models.DO_NOTHING, db_column='id_eestadual', blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'aluno'


class Contato(models.Model):
    id_contato = models.AutoField(primary_key=True)
    tel_aluno = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone do Aluno")
    tel_mae = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone da Mãe")
    tel_pai = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone do Pai")
    tel_recado = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone Recado")
    num_whatsapp = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número Whatsapp")
    email = models.CharField(max_length=70)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'contato'


class Cursos(models.Model):
    id_cursos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45, verbose_name="Nome do Curso")
    dia_semana = models.CharField(max_length=20, verbose_name="Dia da Semana")
    horario = models.CharField(max_length=20, verbose_name="Horário")

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'cursos'


class Eestadual(models.Model):
    NIVEL_CHOICES = [
        ["Fundamental II", "Fundamental II"],
        ["Médio", "Médio"],
        ["EJA", "EJA"]
    ]
    id_eestadual = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, verbose_name="Nome da Escola")
    serie = models.CharField(max_length=2, verbose_name="Série")
    nivel = models.CharField(max_length=15, verbose_name="Nível", choices=NIVEL_CHOICES)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'eestadual'


class Endereco(models.Model):
    LOGRADOURO_CHOICES = [
        ["Alameda", "Alameda"], ["Avenida", "Avenida"], ["Chácara", "Chácara"], ["Estrada", "Estrada"],
        ["Praça", "Praça"], ["Recanto", "Recanto"], ["Rua", "Rua"], ["Sítio", "Sítio"], ["Viela", "Viela"]
    ]
    id_endereco = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=15, choices=LOGRADOURO_CHOICES)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, verbose_name="Número")
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=50)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'endereco'
