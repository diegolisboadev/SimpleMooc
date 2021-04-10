from django import forms

class ContatoCursoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea, required=False) # Field input text how textarea