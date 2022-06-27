import email
from mailbox import NoSuchMailboxError
from pyexpat import model
from tkinter import image_names
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Clientes(models.Model):
    codigo_cliente=models.IntegerField()
    nombre=models.CharField(max_length=40)
    email=models.EmailField()

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    codigo_producto=models.IntegerField()
    descripcion=models.CharField(max_length=40)
    subproducto=models.CharField(max_length=40)

    def __str__(self):
        return self.codigo_producto

class Sucursales(models.Model):
    codigo_sucursal=models.IntegerField()
    sucursal=models.CharField(max_length=40)
    region=models.CharField(max_length=20)

    def __str__(self):
        return self.sucursal

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)