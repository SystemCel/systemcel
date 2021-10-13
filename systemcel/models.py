# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

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
    id_endereco = models.ForeignKey('Endereco', models.DO_NOTHING, db_column='id_endereco', blank=True, null=True)
    id_contato = models.ForeignKey('Contato', models.DO_NOTHING, db_column='id_contato', blank=True, null=True)
    id_eestadual = models.ForeignKey('Eestadual', models.DO_NOTHING, db_column='id_eestadual', blank=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        managed = False
        db_table = 'aluno'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
