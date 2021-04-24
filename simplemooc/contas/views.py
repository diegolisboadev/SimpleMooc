from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings

from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autentica o usuario logo no registro
            user = authenticate(
                username=user.username, 
                password=form.cleaned_data['password1']
            )
            login(request, user) # Logar o usuário após registro/atentificação
            return redirect(settings.LOGIN_URL)
    else:
        form = RegisterForm()

    return render(request, 'contas/register.html', {'form': form})
