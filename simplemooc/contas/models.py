#from contas.forms import User
from typing import cast
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
import re

from django.db.models.base import Model
from django.conf import settings
from django.db.models.deletion import CASCADE

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('Nome de Usuário', max_length=30, unique=True,
    validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), 
    'O nome de usuário só pode conter letras digitos ou os seguintes caracteres @/ ./+/-/_', 'invalid')])
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está Ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def short_name(self):
        return self.username

    def full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', on_delete=CASCADE,
    related_name="resets")
    # related_name="resets" -> nome a ser usado para buscar os dados do model de relacionamento
    key = models.CharField('Chave', max_length=100, unique=True)
    confirmed = models.BooleanField('Confirmado', default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} em {self.created_at}'

    class Meta:
        verbose_name = "Nova Senha"
        verbose_name_plural = "Novas Senhas"
        ordering = ['-created_at'] # - field -> Ordem descrescente