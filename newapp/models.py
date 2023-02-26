from django.db import models
from datetime import datetime, date
# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    correo = models.EmailField(max_length=200)
    contrasena = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    descripcion = models.CharField(models.TextField, max_length=1000)
    ultima_conexion = models.DateTimeField(auto_now=datetime.now())
    creacion_pefil = models.DateTimeField(auto_now_add=datetime.now())
    seguidores = models.IntegerField(default=0)
    seguidos = models.IntegerField(default=0)

    def __str__(self):
        return self.usuario + " - " + self.correo
    
    def contrasenaGet(self):
        return self.contrasena
