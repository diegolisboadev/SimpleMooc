from django import forms
from django.core.mail import send_mail
from django.conf import settings

from core.mail import send_mail_template

class ContatoCursoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem/Dúvida', widget=forms.Textarea, required=False) # Field input text how textarea

    def send_email(self, curso):
        subject = f'Contato do Curso de [{curso}]'
        context = {
            'nome': self.cleaned_data['nome'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        
        send_mail_template(subject, 'cursos/contato_email.html', context, [settings.CONTACT_EMAIL])