from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.titulo
    
class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True, null=False)
    contenido = models.TextField(null=False)
    resumen = models.TextField(max_length=600, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    autor = models.models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/", null=False)
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    permitir_comentarios = models.BooleanField(default=True)

## Del pdf complementario n2 pagina 5, agregar los siguientes campos:
## class Meta
## def __str__(self)
##def delete()
