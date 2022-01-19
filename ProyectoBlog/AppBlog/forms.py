from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BloggerFormulario(forms.Form):
#    usuario = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=20)
    sitio_web = forms.URLField()
    compania = forms.CharField(max_length=20)
    acerca = forms.CharField(widget=forms.Textarea)

class PosteoFormulario(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=50)
    contenido = forms.CharField(widget=forms.Textarea)
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):

    #Obligatorios
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput) 
   
   #Extra
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        
        # Elimina los mensajes de ayuda.
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
        
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'last_name', 'first_name')