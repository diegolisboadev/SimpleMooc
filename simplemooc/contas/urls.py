from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import register

app_name = 'contas' # Necessário para usar o namespace na url principal
urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='contas/login.html'), name="entrar"),
    path('cadastre-se/', register, name="registrar"),
    path('sair/', LogoutView.as_view(next_page='core:home'), name="sair")
]

# Chamo os metodos para criar a view de login interna usando o auth do django view com LoginView.as_view
#(template_name="view_local") -> substitui a view de login original do django por outra definida por mim