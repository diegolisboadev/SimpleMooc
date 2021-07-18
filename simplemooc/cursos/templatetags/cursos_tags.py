
# Criando Template Tags

from django.template.library import Library

from cursos.models import Inscricao

register = Library()

@register.inclusion_tag('templatetags/my_cursos.html') # Transformar uma função em uma tag a ser usada pelo django/jinja (INcluindo HTML)
def my_cursos(user):
    inscricoes = Inscricao.objects.filter(user=user)
    return {'inscricoes': inscricoes}

@register.simple_tag
def load_my_cursos(user):
    return Inscricao.objects.filter(user=user)