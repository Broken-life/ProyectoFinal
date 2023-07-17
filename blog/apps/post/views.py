from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Comentario, Articulo, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Articulo, Categoria




# Aca van las vistas de la app post (Basic Views - Function Based Views)

#ejemplo
def index(request):
    titulo = "soy un título"
    subtitulo = "soy un subtítulo"
    return render(request, 'post/post.html',{
        "titulo":titulo,
        "subtitulo":subtitulo,
    })
    
def crear_articulo(request):
    articulos = Articulo(
        titulo = "primer título",
        contenido="este es el primer contenido del blog.",
        autor = "soy Gustavo Palacios Meyer",
        
    )
    articulos.save()
    return HttpResponse(f'Articulo creado:{articulos.titulo}')
    
    
    
    
    
  
    
        
    
