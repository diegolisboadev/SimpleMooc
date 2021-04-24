from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    """
        Customização do Form de Registro
        (Criando o próprio form de registro)
    Args:
        UserCreationForm ([type]): [description]
    """
    email = forms.EmailField(label='Email')

    # clean_algumcampo
    # Metodo para validar o campo email buscando se o mesmo já existe ou não
    # também para manipular determinado campo ao salvar e/ou validar
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email

    # Sobrescreve o metodo save() do UserCreationForm para o RegisterForm
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user