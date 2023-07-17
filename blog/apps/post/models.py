from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


##NOTAS##
#Informacion de los modelos: en el pdf complementario n2 pagina 4

#Los __str__ son para que se muestre la informacion que queremos en el admin de django y no el nombre del objeto

class Categoria(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.titulo
    
class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True, null=False)
    contenido = models.TextField(null=False)
    resumen = models.TextField(max_length=600, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="media/", null=False)
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    permitir_comentarios = models.BooleanField(default=True)

    ## Del pdf complementario n2 pagina 5 y 6 sacamos lo siguiente:
    ## El método Meta es una clase anidada que contiene metadatos: En este caso, estamos ordenando los resultados por fecha de creación,actualización, y por último por categoría. El signo menos (-) delante de los campos indica que el orden es descendente."
    ## delete es para que cuando se borre un post se borre la imagen tambien

    class Meta:
        ordering = ["-fecha_creacion","-fecha_actualizacion", "categoria"]  

    def __str__(self):
        return self.titulo
    
    def delete(self, *args):
        self.imagen.delete()
        super().delete(*args)

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField(null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    ## Meta para ordenar los comentarios por fecha de creacion y actualizacion
    ## delete es para borrar todo el comentario
    class Meta:
        ordering = ["-fecha_creacion","-fecha_actualizacion"]

    def __str__(self):
        return self.contenido
    
    def delete(self, *args):
        super().delete(*args)
        
class User(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
            