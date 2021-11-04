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

    # id_aluno = models.AutoField(primary_key=False)
    cpf = CPFField(unique=True, verbose_name="CPF (Somente Números):")
    # cpf = models.CharField(unique=True, max_length=14, verbose_name="Número do CPF")
    p_nome = models.CharField(max_length=45, verbose_name="Primeiro Nome")
    sobrenome = models.CharField(max_length=100)
    dt_nasc = models.DateField(verbose_name="Data de Nascimento")
    numero_rg = models.CharField(max_length=9, blank=True, null=True, verbose_name="Número do RG")
    numero_ra = models.CharField(max_length=14, verbose_name="Número do RA")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    # usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return "{} ({} {})".format(self.cpf, self.p_nome, self.sobrenome)

    class Meta:
        managed = False
        db_table = 'aluno'


class Contato(models.Model):
    # id_contato = models.AutoField(primary_key=False)
    tel_aluno = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone do Aluno")
    tel_mae = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone da Mãe")
    tel_pai = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone do Pai")
    tel_recado = models.CharField(max_length=10, blank=True, null=True, verbose_name="Telefone Recado")
    num_whatsapp = models.CharField(max_length=10, blank=True, null=True, verbose_name="Número Whatsapp")
    email = models.CharField(max_length=70)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    # usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'contato'


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


class Eestadual(models.Model):
    NIVEL_CHOICES = [
        ["Fundamental II", "Fundamental II"],
        ["Médio", "Médio"],
        ["EJA", "EJA"]
    ]
    # id_eestadual = models.AutoField(primary_key=False)
    nome = models.CharField(max_length=100, verbose_name="Nome da Escola")
    serie = models.CharField(max_length=2, verbose_name="Série")
    nivel = models.CharField(max_length=15, verbose_name="Nível", choices=NIVEL_CHOICES)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    # usuario = models.OneToOneField(User, on_delete=models.PROTECT)

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
    # id_endereco = models.AutoField(primary_key=False)
    logradouro = models.CharField(max_length=15, choices=LOGRADOURO_CHOICES)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10, verbose_name="Número")
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    # usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'endereco'


class Inscricao(models.Model):
    # Field name made lowercase.
    aluno_cpf = models.CharField(
        db_column='Aluno_cpf', primary_key=True, max_length=11)
    id_endereco = models.IntegerField()
    id_contato = models.IntegerField()
    id_eestadual = models.IntegerField()
    id_cursos = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        managed = False
        db_table = 'inscricao'
        unique_together = (('aluno_cpf', 'id_endereco',
                            'id_contato', 'id_eestadual', 'id_cursos'),)
