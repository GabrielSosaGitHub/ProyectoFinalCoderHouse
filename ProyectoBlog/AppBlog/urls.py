from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path('inicio', views.inicio, name='Inicio'),
               
]