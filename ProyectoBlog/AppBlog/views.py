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

@login_required
def posteoFormulario(request):
    if request.method == 'POST':

        formulario = PosteoFormulario(request.POST, request.FILES)

        if formulario.is_valid():

                informacion = formulario.cleaned_data

#                usuario = None

#                if request.user.is_authenticated():
                usuario = request.user
                autor = Blogger.objects.get(usuario=usuario)

                posteo = Posteo(
                    titulo=informacion['titulo'],
                    subtitulo=informacion['subtitulo'],
                    autor=autor,
                    contenido=informacion['contenido'],
                    imagen=informacion['imagen'])               
                posteo.save()
                
                return render(request, 'inicio.html')
    else:

            formulario = PosteoFormulario()

    esBlogger = False

    if Blogger.objects.filter(usuario=request.user.id):

        esBlogger = True

    return render(request, 'AppBlog/posteoFormulario.html',{"formulario":formulario, "esBlogger":esBlogger})

@login_required
def editarPosteo(request, posteo_id):
    
    posteo = Posteo.objects.get(id=posteo_id)

    if request.method == "POST":
        formulario = PosteoFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            informacion = formulario.cleaned_data

            posteo.titulo = informacion['titulo']
            posteo.subtitulo = informacion['subtitulo']
            posteo.contenido = informacion['contenido']
            posteo.imagen = informacion['imagen']
            
            posteo.save()

            return render(request, 'inicio.html')

    else:

        formulario = PosteoFormulario(initial={'titulo': posteo.titulo, 'subtitulo':posteo.subtitulo, 'contenido': posteo.contenido, 'imagen': posteo.imagen})
        
        
    return render(request, 'AppBlog/editarPosteo.html', {'formulario': formulario, "posteo_id":posteo_id})

############## Vistas asociadas al modelo Blogger ##############
# Listado de bloggers.
class BloggersLista(ListView):
    
    model = Blogger
    template_name = "AppBlog/blogger_list.html"
    
# Detalle del blogger.
class BloggerDetalle(DetailView):
    
    model = Blogger
    template_name = "AppBlog/blogger_detail.html"
    
# Crear blogger.
class BloggerCrear(CreateView):
    
    model = Blogger
    success_url = "./blogger/list"
    fields = ["usuario", "telefono", "direccion", "pais", "ciudad", "sitio_web", "compania", "acerca"]

# Editar blogger.
class BloggerEditar(UpdateView):
    
    model = Blogger
    success_url = "../blogger/list"
    fields = ["usuario", "telefono", "direccion", "pais", "ciudad", "sitio_web", "compania", "acerca"]
  
# Eliminar blogger.   
class BloggerEliminar(DeleteView):
    
    model = Blogger
    success_url = "../blogger/list"

@login_required
def bloggerFormulario(request):
    if request.method == 'POST':

        formulario = BloggerFormulario(request.POST)

        if formulario.is_valid():

                informacion = formulario.cleaned_data

#                usuario = None

#                if request.user.is_authenticated():
                usuario = request.user

                blogger = Blogger(
                    usuario=usuario,
                    telefono=informacion['telefono'],
                    direccion=informacion['direccion'],
                    pais=informacion['pais'],
                    ciudad=informacion['ciudad'],
                    sitio_web=informacion['sitio_web'],
                    compania=informacion['compania'],
                    acerca=informacion['acerca'])               
                blogger.save()
                
                return render(request, 'inicio.html')
    else:

            formulario = BloggerFormulario()

    return render(request, 'AppBlog/bloggerFormulario.html',{"formulario":formulario})

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