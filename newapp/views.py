from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from .models import Usuario
from datetime import datetime, date

# Create your views here

def fechaActual ():
    
    now = datetime.now()
    fechaAct = now.strftime("%Y-%m-%d")
    return fechaAct

def existeCorreo(input):
    users = Usuario.objects.filter(correo=input)
    if len(users) == 0:
        return False
    else:
        return True
    
def existeUsuario(input):
    users = Usuario.objects.filter(usuario=input)
    if len(users) == 0:
        return False
    else:
        return True
  

def iniciarSesion(request):
    fecha_actual = fechaActual()
    if request.method == 'GET':
        return render(request, "index.html", {"fecha_actual":fecha_actual})
    else:
        users = Usuario.objects.filter(correo=request.POST.get('ICorreo'))
        cantUsuario = len(users)
        if cantUsuario != 0:
            usuario = Usuario.objects.get(correo=request.POST['ICorreo'])
            if usuario.contrasenaGet() == request.POST['IContrasena'] :
                usuario.save()
                return    render(request, "perfil.html", {'usuario':usuario, "fecha_actual":fecha_actual})
            else:
                Icorreo = ""
                Icontrasena = "Contraseña no existe"
                return render(request, "index.html",{"Icorreo":Icorreo, "Icontrasena":Icontrasena, "fecha_actual":fecha_actual} )
        else:
            Icorreo = "Correo Erroneo"
            Icontrasena = ""
            return render(request, "index.html",{"Icorreo":Icorreo, "Icontrasena":Icontrasena, "fecha_actual":fecha_actual} )
        
def hello(request):
    fecha_actual = fechaActual()
    return render(request, "index.html" , {"fecha_actual":fecha_actual})

def crearUsuario(request):
    fecha_actual = fechaActual()
    if request.method == 'GET':
        return render(request, "index.html", {"fecha_actual":fecha_actual})
    else:
        Rcorreo = ""
        Rfecha = ""
        Rusuario = ""
        Rcontra = ""

        if existeCorreo(request.POST.get('R-Correo')) == False:
            if len(request.POST.get('R-NombreUsuario')) > 4 and existeUsuario(request.POST.get('R-NombreUsuario')) == False:
                if len(request.POST.get('R-Contrasena')) > 4:
                    if request.POST.get('R-fechaNacimiento') != "1900-01-01":
                        Usuario.objects.create( usuario = request.POST.get('R-NombreUsuario'), correo = request.POST.get('R-Correo'), contrasena = request.POST.get('R-Contrasena'), fecha_nacimiento = request.POST.get('R-fechaNacimiento'), descripcion = "Yo soy " + request.POST.get('R-NombreUsuario'))
                        return render(request, "index.html",{"Rcorreo": Rcorreo, "Rfecha": Rfecha, "fecha_actual":fecha_actual} )
                    else:
                        Rfecha = "Ingresar fecha de nacimiento"
                        return render(request, "index.html",{"Rcorreo": Rcorreo, "Rfecha": Rfecha, "fecha_actual":fecha_actual} )
                else:
                    Rcontra = "Debe tener minimo 5 caracteres"
                    return render(request, "index.html",{"Rcorreo": Rcorreo, "Rfecha": Rfecha, "Rcontra": Rcontra, "fecha_actual":fecha_actual} )
            # Consulta cual es el error al crear el nombre de usuario
            elif len(request.POST.get('R-NombreUsuario')) <= 4 :
                Rusuario = "Debe tener minimo 5 caracteres"
                return render(request, "index.html",{"Rcorreo": Rcorreo, "Rfecha": Rfecha, "Rusuario": Rusuario, "fecha_actual":fecha_actual} )
            else:
                Rusuario = "Nombre de usuario ya existe"
                return render(request, "index.html",{"Rcorreo": Rcorreo, "Rfecha": Rfecha, "Rusuario": Rusuario, "fecha_actual":fecha_actual} )
        else:
            Rcorreo = "Correo ya existe"
            return render(request, "index.html",{"Rcorreo": Rcorreo, "Rfecha": Rfecha, "fecha_actual":fecha_actual} )
