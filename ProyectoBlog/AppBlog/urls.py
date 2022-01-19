from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),

    path('posteo/list', views.PosteosLista.as_view(), name='PosteosLista'),
    path(r'^detallePosteo/(?P<pk>\d+)$', views.PosteoDetalle.as_view(), name='PosteoDetalle'),
    path(r'^nuevoPosteo$', views.PosteoCrear.as_view(), name='PosteoCrear'),
    path(r'^editarPosteo/(?P<pk>\d+)$', views.PosteoEditar.as_view(), name='PosteoEditar'),
    path(r'^borrarPosteo/(?P<pk>\d+)$', views.PosteoEliminar.as_view(), name='PosteoEliminar'),

    path('blogger/list', views.BloggersLista.as_view(), name='BloggersLista'),
    path(r'^detalleBlogger/(?P<pk>\d+)$', views.BloggerDetalle.as_view(), name='BloggerDetalle'),
    path(r'^nuevoBlogger$', views.BloggerCrear.as_view(), name='BloggerCrear'),
    path(r'^editarBlogger/(?P<pk>\d+)$', views.BloggerEditar.as_view(), name='BloggerEditar'),
    path(r'^borrarBlogger/(?P<pk>\d+)$', views.BloggerEliminar.as_view(), name='BloggerEliminar'),

    path('login', views.login_request, name='Login'),
    path('register', views.register, name="Register"),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name="Logout"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
               
]