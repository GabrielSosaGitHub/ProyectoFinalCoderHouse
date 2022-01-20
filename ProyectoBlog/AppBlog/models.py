from asyncio.windows_events import NULL
from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Blogger(models.Model):

    usuario = models.ForeignKey(User, on_delete= models.CASCADE, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=40)
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    sitio_web = models.URLField()
    compania = models.CharField(max_length=20)
    acerca = models.TextField()
    registrado = models.DateTimeField(auto_now_add=True)
    foto = models.ImageField()
    
    def __str__(self):
        return f"Blogger: {self.usuario.username}. Email: {self.usuario.email}. Registrado: {self.registrado}."

class Posteo(models.Model):

    titulo = models.CharField(max_length=50, unique=True)
    subtitulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Blogger, on_delete= models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    imagen = models.ImageField()

    def __str__(self):
        return f"Título: {self.titulo}. Blogger: {self.autor.usuario.username}. Creado: {self.creado}. Actualizado: {self.actualizado}."