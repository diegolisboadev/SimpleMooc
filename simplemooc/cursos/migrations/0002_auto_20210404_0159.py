# Generated by Django 3.1.7 on 2021-04-04 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='data_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data Inicio'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='cursos/imagens', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nome',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='slug',
            field=models.SlugField(verbose_name='Atalho'),
        ),
    ]
