# Generated by Django 3.1.7 on 2021-03-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField()),
                ('descricao', models.TextField(blank=True)),
                ('data_inicio', models.DateField(blank=True, null=True)),
                ('imagem', models.ImageField(upload_to='cursos/imagens', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
