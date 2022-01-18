from socket import fromshare
from django import forms

class BloggerFormulario(forms.Form):
    usuario = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=15)
    direccion = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=20)
    sitio_web = forms.URLField()
    compania = forms.CharField(max_length=20)
    acerca = forms.TextField()


class PosteoFormulario(forms.Form):
    titulo = forms.CharField(max_length=200, unique=True)
    autor = forms.CharField(max_length=50)
    contenido = forms.TextField()
    imagen = forms.ImageField()

    def __str__(self):
        return f"Título: {self.titulo}. Blogger: {self.autor.usuario.username}. Creado: {self.creado}. Actualizado: {self.actualizado}."

