from django.db import models


class Aluno(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das Opções"]
    ]

    id_aluno = models.AutoField(primary_key=True)
    cpf = models.CharField(unique=True, max_length=11)
    p_nome = models.CharField(max_length=45)
    sobrenome = models.CharField(max_length=100)
    dt_nasc = models.DateField()
    numero_rg = models.CharField(max_length=9, blank=True, null=True)
    numero_ra = models.CharField(max_length=14)
    nome_mae = models.CharField(max_length=100, verbose_name="Mãe")
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
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
    tel_aluno = models.CharField(max_length=10, blank=True, null=True)
    tel_mae = models.CharField(max_length=10, blank=True, null=True)
    tel_pai = models.CharField(max_length=10, blank=True, null=True)
    tel_recado = models.CharField(max_length=10, blank=True, null=True)
    num_whatsapp = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=70)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'contato'


class Cursos(models.Model):
    id_cursos = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    dia_semana = models.CharField(max_length=15)
    horario = models.CharField(max_length=5)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'cursos'




class Eestadual(models.Model):
    id_eestadual = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    serie = models.CharField(max_length=2)
    nivel = models.CharField(max_length=15)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'eestadual'


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    logradouro = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    cep = models.CharField(max_length=9)
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=50)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        managed = False
        db_table = 'endereco'
