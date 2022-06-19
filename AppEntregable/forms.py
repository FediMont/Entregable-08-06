from django import forms
from AppEntregable.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields}

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nombre_de_usuario = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=50)
    fecha_de_nacimiento = forms.DateField()

class Biblio_form(forms.ModelForm):
    class Meta:
        model = Bibliotecas
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'apertura': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control', 'placeholder':"http://www.ejemplo.com"}),
            'imagen': forms.URLInput(attrs={'class':'form-control', 'placeholder':"Dirección web de imagen"}),
        }

class Libro_form(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
        widgets = {
            'nombre_libro': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'link_autor': forms.URLInput(attrs={'class':'form-control', 'placeholder':"http://www.ejemplo.com"}),
            'link_texto': forms.URLInput(attrs={'class':'form-control', 'placeholder':"http://www.ejemplo.com"}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
        }