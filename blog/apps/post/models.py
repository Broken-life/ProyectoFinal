from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True, null=False)
    contenido = models.TextField(null=False)
    resumen = models.TextField(max_length=600, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    autor = models.models.ForeignKey("app.User", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/", null=False)
    publicado 
    categoria 
    fecha_actualizacion