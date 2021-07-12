from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cursos, Inscricao
from .forms import ContatoCursoForm

# Create your views here.

def cursos(request):
    return render(request, 'cursos/cursos.html', {
        'cursos': Cursos.objects.all(),
    })

def detalhes_curso(request, slug): #pk
    # get_object_or_404() -> Retornar o objeto caso exista se não retornar a page 404
    curso = get_object_or_404(Cursos, slug=slug)
    if request.method == 'POST':
        formContato = ContatoCursoForm(request.POST)

        if formContato.is_valid():
            formContato.send_email(curso)
            print(formContato.cleaned_data)
    else:
        formContato = ContatoCursoForm()
    return render(request, 'cursos/detalhes.html', {
            'curso': curso,
            'formContato': formContato
    }) #pk=pk

@login_required
def inscricao(request, slug):
    curso = get_object_or_404(Cursos, slug=slug)
    inscricao, criacao = Inscricao.objects.get_or_create(user=request.user, curso=curso)
    if criacao:
        messages.success(request, 'Você foi inscrito no Curso!')
    else:
        messages.info(request, 'Você já está inscrito nesse Curso!')
    # inscricao.ativo()
    return redirect('contas:dashboard')