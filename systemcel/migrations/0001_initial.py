# Generated by Django 3.2.7 on 2021-10-10 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('p_nome', models.CharField(max_length=45)),
                ('sobrenome', models.CharField(max_length=100)),
                ('dt_nasc', models.DateField()),
                ('numero_rg', models.CharField(blank=True, max_length=9, null=True)),
                ('numero_ra', models.CharField(max_length=20)),
                ('nome_mae', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id_contato', models.AutoField(primary_key=True, serialize=False)),
                ('tel_aluno', models.CharField(blank=True, max_length=10, null=True)),
                ('tel_mae', models.CharField(blank=True, max_length=10, null=True)),
                ('tel_pai', models.CharField(blank=True, max_length=10, null=True)),
                ('tel_recado', models.CharField(blank=True, max_length=10, null=True)),
                ('num_whatsapp', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'contato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id_cursos', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('dia_semana', models.CharField(max_length=15)),
                ('horario', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'cursos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Eestadual',
            fields=[
                ('id_eestadual', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('serie', models.CharField(max_length=2)),
                ('nivel', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'eestadual',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id_endereco', models.AutoField(primary_key=True, serialize=False)),
                ('logradouro', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=45)),
                ('cidade', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'endereco',
                'managed': False,
            },
        ),
    ]
