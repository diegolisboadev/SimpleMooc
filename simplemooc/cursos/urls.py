from django.urls import path
from cursos.views import cursos, detalhes_curso, inscricao

app_name = 'cursos'
urlpatterns = [
    path('', cursos, name="curso"),
    path('<slug:slug>/detalhes/', detalhes_curso, name="detalhes_cursos"),
    path('<slug:slug>/inscricao/', inscricao, name="inscricao_cursos")
    #path('<int:pk>/detalhes/', detalhes_curso, name="detalhes_cursos")
]