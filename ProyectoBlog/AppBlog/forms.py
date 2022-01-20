from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BloggerFormulario(forms.Form):
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=20)
    sitio_web = forms.URLField()
    compania = forms.CharField(max_length=20)
    acerca = forms.CharField(widget=forms.Textarea)
    foto = forms.ImageField()

class PosteoFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    contenido = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):

    # Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 
   
    # Opcional
    last_name = forms.CharField(label='Nombre',)
    first_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        # Elimina los mensajes de ayuda.
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Apellido")
    first_name = forms.CharField(label="Nombre")
        
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'last_name', 'first_name')