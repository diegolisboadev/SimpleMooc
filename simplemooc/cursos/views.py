from django.shortcuts import render, get_object_or_404
from .models import Cursos
from .forms import ContatoCursoForm

# Create your views here.

def cursos(request):
    return render(request, 'cursos/cursos.html', {
        'cursos': Cursos.objects.all(),
    })

def detalhes_curso(request, slug): #pk
    # get_object_or_404() -> Retornar o objeto caso exista se não retornar a page 404
    if request.method == 'POST':
        formContato = ContatoCursoForm(request.POST)

        if formContato.is_valid():
            print(formContato.cleaned_data)
    else:
        formContato = ContatoCursoForm()
    return render(request, 'cursos/detalhes.html', {
            'curso': get_object_or_404(Cursos, slug=slug),
            'formContato': formContato
    }) #pk=pk