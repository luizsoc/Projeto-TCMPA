# Generated by Django 5.1.5 on 2025-02-26 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_cargo', models.CharField(max_length=255)),
                ('vagas_autorizadas', models.IntegerField(default=0)),
                ('vagas_ocupadas', models.IntegerField(default=0)),
                ('cbo', models.CharField(max_length=10)),
                ('quadro_cargos', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_exibicao', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=18)),
                ('tipo_orgao', models.CharField(max_length=100)),
                ('municipio', models.CharField(max_length=255)),
                ('codigo_ibge', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuadroCargos',
            fields=[
                ('codigo_controle', models.AutoField(primary_key=True, serialize=False)),
                ('nome_quadro', models.CharField(max_length=255)),
            ],
        ),
    ]
