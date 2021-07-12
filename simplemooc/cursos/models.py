from enum import unique
from random import choices
from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE

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

    # Recebe a var setada e gerar uma url_absolute
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("cursos:detalhes_cursos", kwargs={"slug": self.slug})
        #return reverse("model_detail", kwargs={"pk": self.pk})
    
    # Class Meta
    class Meta:
        db_table = 'tb_mooc_cursos'
        app_label = 'cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos' 
        ordering = ['nome'] # Ordernar os dados na tabela de cursos em ordem crescente -name (orderDesc)

class Inscricao(models.Model):

    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovado'),
        (2, 'Cancelado')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Inscrição', 
        related_name='inscricao',
        on_delete=CASCADE
    )

    curso = models.ForeignKey(Cursos, verbose_name='Curso', related_name="curso", on_delete=CASCADE)
    status = models.IntegerField('Situação', choices=STATUS_CHOICES, default=1, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def ativo(self):
        self.status = 1
        self.save()

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        unique_together = (('user', 'curso'))
        # Campos unicos no BD -> Não permite 2 cursos iguais para o mesmo usuário na relação