# Generated by Django 5.1.5 on 2025-01-24 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_municipio_orgao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quadrocargos',
            options={},
        ),
        migrations.AlterField(
            model_name='quadrocargos',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Status'),
        ),
    ]
