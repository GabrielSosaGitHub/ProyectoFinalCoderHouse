from django.shortcuts import render

# Importo los modelos.
from AppBlog.models import *

# Importo los formularios.
from AppBlog.forms import *

# Necesario para listar con CBV:
from django.views.generic import ListView

# Necesario para ver detalles con CBV:
from django.views.generic.detail import DetailView

# Necesario para crear, modificar y borrar clases respectiavamente con CBV:
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Necesario para login, logout y registro.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Decorador de Django por defecto
from django.contrib.auth.decorators import login_required

# Create your views here.

# Vista de inicio.
def inicio(request):
    return render(request, 'inicio.html')

############## Vistas asociadas al modelo Posteo ##############
# Listado de posteos.
class PosteosLista(ListView):
    
    model = Posteo
    template_name = "AppBlog/posteo_list.html"
    
# Detalle de posteo.
class PosteoDetalle(DetailView):
    
    model = Posteo
    template_name = "AppBlog/posteo_detail.html"
    
# Crear posteo.
class PosteoCrear(CreateView):
    
    model = Posteo
    success_url = "./posteo/list"
#    fields = ["titulo", "subtitulo", "autor", "contenido", "imagen"]
    fields = ["titulo", "subtitulo", "autor", "contenido"]

# Editar posteo.
class PosteoEditar(UpdateView):
    
    model = Posteo
    success_url = "../posteo/list"
#    fields = ["titulo", "subtitulo", "autor", "contenido", "imagen"]
    fields = ["titulo", "subtitulo", "autor", "contenido"]
  
# Eliminar posteo.   
class PosteoEliminar(DeleteView):
    
    model = Posteo
    success_url = "../posteo/list"

############## Vistas asociadas al modelo Blogger ##############
# Listado de posteos.
class BloggersLista(ListView):
    
    model = Blogger
    template_name = "AppBlog/blogger_list.html"
    
# Detalle de posteo.
class BloggerDetalle(DetailView):
    
    model = Blogger
    template_name = "AppBlog/blogger_detail.html"
    
# Crear posteo.
class BloggerCrear(CreateView):
    
    model = Blogger
    success_url = "./blogger/list"
    fields = ["usuario", "telefono", "direccion", "pais", "ciudad", "sitio_web", "compania", "acerca"]

# Editar posteo.
class BloggerEditar(UpdateView):
    
    model = Blogger
    success_url = "../blogger/list"
    fields = ["usuario", "telefono", "direccion", "pais", "ciudad", "sitio_web", "compania", "acerca"]
  
# Eliminar posteo.   
class BloggerEliminar(DeleteView):
    
    model = Blogger
    success_url = "../blogger/list"

############## Vistas asociadas a login, logout y registro ##############
def login_request(request):
    
    if request.method =="POST":
        
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            
            user = authenticate(username=usuario, password = contrasenia)
            
            if user is not None:
                
                login(request, user)
                
                return render(request, "inicio.html", {"mensaje":f'Iniciaste sesión como {usuario}.'})
                
            else:
                
                return render(request, "inicio.html", {"mensaje":"Los datos ingresados son incorrectos."})
                
            
        else:
            
            return render(request, "inicio.html", {"mensaje":"Formulario erróneo."})
            
            
    
    
    form = AuthenticationForm()  #Formulario sin nada para hacer el login
    
    return render(request, "AppBlog/login.html", {"form":form} )


def register(request):

    if request.method == 'POST':
            
        form = UserRegisterForm(request.POST)
            
        if form.is_valid():

            username = form.cleaned_data['username']
                                    
            form.save()
                  
            return render(request,"inicio.html",  {"mensaje":f"¡{username} fue creado exitosamente!"})

    else:
             
            form = UserRegisterForm()     

    return render(request,"AppBlog/register.html" ,  {"form":form})


@login_required
def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':
        
        formulario = UserEditForm(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()
            
             
            return render(request, "inicio.html")
            
    else:
        
        formulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, "AppBlog/editarPerfil.html", {"formulario":formulario, "usuario":usuario})   