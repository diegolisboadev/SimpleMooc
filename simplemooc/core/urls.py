from django.urls import path
from core.views import home, contato

app_name = 'core' # Necessário para o reconhecimento do namespace
urlpatterns = [
    path('', home, name="home"),
    path('contato/', contato, name="contato"),
]