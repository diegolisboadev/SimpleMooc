# Generated by Django 3.1.7 on 2021-07-12 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_auto_20210712_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscricao',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], default=1, verbose_name='Situação'),
        ),
    ]
