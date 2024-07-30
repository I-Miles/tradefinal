from django import forms
from .models import Contact,Cliente
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'carro', 'servico','telefone']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class UserRegisterForm(UserCreationForm):
    # Adição de um campo de e-mail ao formulário, marcado como obrigatório
    email = forms.EmailField(required=True)
    # Definição da classe Meta
    class Meta:
        model = User
        # Define os campos que serão exibidos no formulário, na ordem especificada
        fields = ('username', 'email', 'password1', 'password2')