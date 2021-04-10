from django.shortcuts import render, get_object_or_404
from .models import Cursos

# Create your views here.

def cursos(request):
    return render(request, 'cursos/cursos.html', {'cursos': Cursos.objects.all()})

def detalhes_curso(request, slug): #pk
    # get_object_or_404() -> Retornar o objeto caso exista se não retornar a page 404
    return render(request, 'cursos/detalhes.html', {'curso': get_object_or_404(Cursos, slug=slug)}) #pk=pk