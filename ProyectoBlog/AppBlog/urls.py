from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
    path('configuracionCuenta', views.configuracionCuenta, name='ConfiguracionCuenta'),
    path('about', views.about, name='About'),

    # Posteos
    path('listaPosteos', views.listaPosteos, name='ListaPosteos'),
    path(r'^detallePosteo/(?P<pk>\d+)$', views.PosteoDetalle.as_view(), name='PosteoDetalle'),
    path('posteoFormulario', views.posteoFormulario, name='PosteoFormulario'),
    path('eliminarPosteo/<posteo_id>/', views.eliminarPosteo, name='EliminarPosteo'),
    path('confirmaEliminarPosteo/<posteo_id>/', views.confirmaEliminarPosteo, name='ConfirmaEliminarPosteo'),
    path('editarPosteo/<posteo_id>/', views.editarPosteo, name='EditarPosteo'),

    # Bloggers
    path('blogger/list', views.BloggersLista.as_view(), name='BloggersLista'),
    path(r'^detalleBlogger/(?P<pk>\d+)$', views.BloggerDetalle.as_view(), name='BloggerDetalle'),
    path('bloggerFormulario', views.bloggerFormulario, name='BloggerFormulario'),
    path('eliminarBlogger/<blogger_id>/', views.eliminarBlogger, name='EliminarBlogger'),
    path('confirmaEliminarBlogger/<blogger_id>/', views.confirmaEliminarBlogger, name='ConfirmaEliminarBlogger'),
    path('editarBlogger/<blogger_id>/', views.editarBlogger, name='EditarBlogger'),

    path('login', views.login_request, name='Login'),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
               
]