from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'usuario': 'Diego'})
    # return HttpResponse('Olá Mundo!')

def contato(request):
    return render(request, 'contato.html')