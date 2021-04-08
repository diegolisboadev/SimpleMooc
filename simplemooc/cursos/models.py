from django.db import models

# Create your models here.

class CursosManager(models.Manager):
    def buscar(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) 
            | models.Q(descricao__icontains=query)
        ) # Reflete select com where ou like (usando or)

        '''return self.get_queryset().filter(
            nome__icontains=query,
            descricao__icontains=query
        ) # Reflete select com where ou like (usando and)'''

class Cursos(models.Model):
    nome = models.CharField("Nome", max_length=100, blank=True, null=True)
    slug = models.SlugField("Atalho")
    descricao = models.TextField("Descricao", blank=True)
    sobre = models.TextField("Sobre", blank=True, null=True)
    data_inicio = models.DateField("Data Inicio", null=True)
    imagem = models.ImageField("Imagem", upload_to="cursos/imagens", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Habilitando o Custom Manager - será usado no lugar do objects manager padrão do Django 
    objects = CursosManager()

    # Alterar o nome dos objetos do Curso na Aplicação View e Admin
    def __str__(self):
        return self.nome
    

    # Class Meta
    class Meta:
        db_table = 'tb_mooc_cursos'
        app_label = 'cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos' 
        ordering = ['nome'] # Ordernar os dados na tabela de cursos em ordem crescente -name (orderDesc)