
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello , name="login1"),
    path('login/', views.iniciarSesion , name="login"),
    path('crear/', views.crearUsuario , name="crearUsuario"),
]