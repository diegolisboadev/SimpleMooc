from django.urls import path
from cursos.views import cursos, detalhes_curso

app_name = 'cursos'
urlpatterns = [
    path('', cursos , name="cursos"),
    path('<int:pk>/detalhes/', detalhes_curso, name="detalhes_cursos")
]