from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import leitor

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=200)
    endereco = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        # Criação do usuário
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        
        # Criação do leitor (se necessário)
        leitor_instance = leitor(
            user=user,
            nome=self.cleaned_data['nome'],
            endereco=self.cleaned_data['endereco']
        )
        if commit:
            leitor_instance.save()
        
        return user

class LoginForm(forms.Form):
    username = forms.CharField(label="Nome de Usuário", max_length=200)  # Usa 'username' que é o 'ref_Id'
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)