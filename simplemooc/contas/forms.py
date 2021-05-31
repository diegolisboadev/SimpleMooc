from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .models import PasswordReset
from core.utils import generate_hash_key
from core.mail import send_mail_template


User = get_user_model()

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Email')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        
        # Envio do Email
        template_name = 'contas/password_reset_email.html'
        subject = 'Criar nova senha no SimpleMooc'
        context = { 'reset': reset }
        send_mail_template(subject, template_name, context, [user.email])

    # Validar Email - Já Cadastrado True or False
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        return forms.ValidationError(
            "Nenhum usuário encontrado com este email!"
        )

class RegisterForm(forms.ModelForm): # UserCreationForm
    """
        Customização do Form de Registro
        (Criando o próprio form de registro)
    Args:
        UserCreationForm ([type]): [description]
    """
    # email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de senha', widget=forms.PasswordInput)

    #
    def cleaned_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'A confirmação não está correta',
                code='password_mismatch'
            )
        return password2

    # clean_algumcampo
    # Metodo para validar o campo email buscando se o mesmo já existe ou não
    # também para manipular determinado campo ao salvar e/ou validar
    '''def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email'''

    # Sobrescreve o metodo save() do UserCreationForm para o RegisterForm
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        #user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username']

class EditAccountForm(forms.ModelForm):
    """ModelForm - serve para gerar um form automaticamente
    do Model na view sem precisar repetir os campos em um form - forms.py

    Obs. queryset -> buscar usuários com o respectivo menos o user atual

    Args:
        forms ([type]): [description]
    """
    '''def clean_email(self):
        """ Clean campo email 
            metodo para validar o email
            caso existar em algum registro 
            excluido a verificão no user atual
        Raises:
            forms.ValidationError: [description]

        Returns:
            [type]: [description]
        """
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Já existe usuário com este E-mail')
        return email'''

    class Meta:
        model = User
        fields = ['username', 'email'] # 'first_name', 'last_name'
