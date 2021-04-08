from django.contrib import admin
from .models import Cursos

# Register your models here.

class CursosAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'data_inicio', 'created_at'] # Defini os head da tabela de cursos do admin
    search_fields = ['nome', 'slug'] # Defini os campos de pesquisa na tabela de Cursos do admin
    prepopulated_fields = {'slug': ('nome')} # Popular determinado campo conforme outro campo

admin.site.register(Cursos)