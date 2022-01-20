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
    posteos = Posteo.objects.all()
    return render(request, 'inicio.html', {"posteos":posteos})

# Vista de inicio.
def about(request):
    return render(request, 'AppBlog/about.html')

# Configuración de la cuenta de usuario.
@login_required
def configuracionCuenta(request):

    esBlogger = False

    if Blogger.objects.filter(usuario=request.user.id):

        esBlogger = True
        blogger = Blogger.objects.get(usuario=request.user)
        return render(request, 'AppBlog/configuracionCuenta.html', {"esBlogger":esBlogger, "blogger_id":blogger.id})

    return render(request, 'AppBlog/configuracionCuenta.html', {"esBlogger":esBlogger})

############## Vistas asociadas al modelo Posteo ##############
# Detalle de posteo.
class PosteoDetalle(DetailView):
    
    model = Posteo
    template_name = "AppBlog/posteo_detail.html"

def listaPosteos(request):

    posteos = Posteo.objects.all()
    return render(request, 'AppBlog/listaPosteos.html', {"posteos":posteos})

@login_required
def posteoFormulario(request):
    if request.method == 'POST':

        formulario = PosteoFormulario(request.POST, request.FILES)

        if formulario.is_valid():

                informacion = formulario.cleaned_data

                usuario = request.user
                autor = Blogger.objects.get(usuario=usuario)

                posteo = Posteo(
                    titulo=informacion['titulo'],
                    subtitulo=informacion['subtitulo'],
                    autor=autor,
                    contenido=informacion['contenido'],
                    imagen=informacion['imagen'])               
                posteo.save()
                
                posteos = Posteo.objects.all()

                return render(request, 'inicio.html', {"posteos":posteos} )
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

            posteos = Posteo.objects.all()

            return render(request, 'inicio.html', {"posteos":posteos})

    else:

        formulario = PosteoFormulario(initial={'titulo': posteo.titulo, 'subtitulo':posteo.subtitulo, 'contenido': posteo.contenido, 'imagen': posteo.imagen})

    esBlogger = False
    esAutor = False

    if Blogger.objects.filter(usuario=request.user.id):

        esBlogger = True

        if Blogger.objects.get(usuario=request.user) == posteo.autor:

            esAutor = True

    if Blogger.objects.filter(usuario=request.user.id) == posteo.autor:

        esAutor = True    
        
    return render(request, 'AppBlog/editarPosteo.html', {'formulario': formulario, "posteo_id":posteo_id, "esBlogger":esBlogger, "esAutor":esAutor})

@login_required
def confirmaEliminarPosteo(request, posteo_id):

    posteo = Posteo.objects.get(id=posteo_id)

    esBlogger = False

    if Blogger.objects.filter(usuario=request.user.id):

        esBlogger = True

        if Blogger.objects.get(usuario=request.user) == posteo.autor:

            esAutor = True

        else:

            esAutor = False

    if Blogger.objects.filter(usuario=request.user.id) == posteo.autor:

        esAutor = True

    return render(request, 'AppBlog/posteo_confirmar_eliminacion.html',{"posteo":posteo, "esBlogger":esBlogger, "esAutor":esAutor})

@login_required
def eliminarPosteo(request, posteo_id):

    paraBorrar = Posteo.objects.get(id=posteo_id)
    paraBorrar.delete()
    posteos = Posteo.objects.all()

    return render(request, 'AppBlog/listaPosteos.html', {"posteos":posteos})

############## Vistas asociadas al modelo Blogger ##############
# Listado de bloggers.
class BloggersLista(ListView):
    
    model = Blogger
    template_name = "AppBlog/blogger_list.html"
    
# Detalle del blogger.
class BloggerDetalle(DetailView):
    
    model = Blogger
    template_name = "AppBlog/blogger_detail.html"
    
@login_required
def bloggerFormulario(request):
    if request.method == 'POST':

        formulario = BloggerFormulario(request.POST, request.FILES)

        if formulario.is_valid():

                informacion = formulario.cleaned_data

                usuario = request.user

                blogger = Blogger(
                    usuario=usuario,
                    telefono=informacion['telefono'],
                    direccion=informacion['direccion'],
                    pais=informacion['pais'],
                    ciudad=informacion['ciudad'],
                    sitio_web=informacion['sitio_web'],
                    compania=informacion['compania'],
                    acerca=informacion['acerca'],
                    foto=informacion['foto'])               
                blogger.save()

                posteos = Posteo.objects.all()
                
                return render(request, 'inicio.html', {"posteos":posteos, "mensaje":f'¡Felicitaciones, {usuario.username}! Ahora formás parte del staff de bloggers &nbsp <i class="far fa-laugh-beam"></i>'})
    else:

            formulario = BloggerFormulario()

    return render(request, 'AppBlog/bloggerFormulario.html',{"formulario":formulario})

@login_required
def editarBlogger(request, blogger_id):
    
    blogger = Blogger.objects.get(id=blogger_id)

    if request.method == "POST":
        formulario = BloggerFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            informacion = formulario.cleaned_data

            blogger.telefono = informacion['telefono']
            blogger.direccion = informacion['direccion']
            blogger.pais = informacion['pais']
            blogger.ciudad = informacion['ciudad']
            blogger.sitio_web = informacion['sitio_web']
            blogger.compania = informacion['compania']
            blogger.acerca = informacion['acerca']
            blogger.foto = informacion['foto']
            
            blogger.save()

            posteos = Posteo.objects.all()
             
            return render(request, "inicio.html", {"mensaje":f'¡Los cambios se realizaron con éxito, {request.user.username}! &nbsp <i class="fas fa-laugh-wink"></i>', "posteos":posteos})

    else:

        formulario = BloggerFormulario(initial={'telefono': blogger.telefono, 'direccion':blogger.direccion, 'pais': blogger.pais, 'ciudad': blogger.ciudad, 'sitio_web':blogger.sitio_web, 'compania':blogger.compania, 'acerca':blogger.acerca, 'foto':blogger.foto})

    return render(request, 'AppBlog/editarBlogger.html', {'formulario': formulario, "blogger_id":blogger_id})

@login_required
def confirmaEliminarBlogger(request, blogger_id):

    blogger = Blogger.objects.get(id=blogger_id)
    return render(request, 'AppBlog/blogger_confirmar_eliminacion.html',{"blogger":blogger})

@login_required
def eliminarBlogger(request, blogger_id):

    paraBorrar = Blogger.objects.get(id=blogger_id)
    paraBorrar.delete()

    return render(request, 'inicio.html', {"posteos":Posteo.objects.all(), "mensaje":f'Ya no sos blogger dentro de la comunidad <i class="fas fa-heart-broken"></i>'})

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

                posteos = Posteo.objects.all()
                
                return render(request, "inicio.html", {"posteos":posteos, "mensaje":f'¡Iniciaste sesión como {usuario}!'})
                
            else:

                return render(request, "inicio.html", {"mensaje":"Formulario erróneo."})
            
        else:

            form = AuthenticationForm(request, data = request.POST)
        
            if form.is_valid():
            
                usuario = form.cleaned_data.get("username")
                contrasenia = form.cleaned_data.get("password")

            return render(request, "AppBlog/login.html", {"mensaje":"Los datos ingresados son incorrectos &nbsp &nbsp <i class='far fa-surprise'></i>"})
            
            
    
    # Formulario vacío para hacer el login.
    form = AuthenticationForm() 
    
    return render(request, "AppBlog/login.html", {"form":form} )


def register(request):

    if request.method == 'POST':
            
        form = UserRegisterForm(request.POST)
            
        if form.is_valid():

            username = form.cleaned_data['username']
                                    
            form.save()

            user = authenticate(username=username, password = form.cleaned_data['password1'])

            login(request, user)

            posteos = Posteo.objects.all()
                  
            return render(request,"inicio.html",  {"posteos":posteos, "mensaje":f"¡{username} fue creado y se ha iniciado sesión exitosamente! <i class='fas fa-fist-raised'></i>"})

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
            
            posteos = Posteo.objects.all()
             
            return render(request, "inicio.html", {"mensaje":f'¡Los cambios se realizaron con éxito, {usuario.username}! &nbsp <i class="fas fa-laugh-wink"></i>', "posteos":posteos})
            
    else:
        
        formulario = UserEditForm(initial={'email':usuario.email})

    esBlogger = False

    if Blogger.objects.filter(usuario=request.user.id):

        esBlogger = True

    if esBlogger == True:

        blogger = Blogger.objects.get(usuario=request.user)      
        return render(request, "AppBlog/editarPerfil.html", {"formulario":formulario, "usuario":usuario, "esBlogger":esBlogger, "blogger_id":blogger.id})

    else:

        return render(request, "AppBlog/editarPerfil.html", {"formulario":formulario, "usuario":usuario, "esBlogger":esBlogger})