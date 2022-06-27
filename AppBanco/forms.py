from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ClienteForm(forms.Form):
    codigo_cliente=forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    email=forms.EmailField()

class ProductoForm(forms.Form):
    codigo_producto=forms.IntegerField()
    descripcion=forms.CharField(max_length=40)
    subproducto=forms.CharField(max_length=40)

class SucursalForm(forms.Form):
    codigo_sucursal=forms.IntegerField()
    sucursal=forms.CharField(max_length=40)
    region=forms.CharField(max_length=20)


class LoginForm(forms.Form):
    username=forms.CharField(label='Usuario', max_length=40)
    password=forms.CharField(label='Password', max_length=40)

class RegistrationForm(UserCreationForm):
    username=forms.CharField(label='Usuario', max_length=40)
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label='Contraseña')
    password2=forms.CharField(label='Repetir contraseña')


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1=forms.CharField(label='Modificar Contraseña')
    password2=forms.CharField(label='Repetir contraseña')

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

