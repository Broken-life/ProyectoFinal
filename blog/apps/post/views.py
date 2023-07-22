from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Comentario, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria




# Aca van las vistas de la app post (Basic Views - Function Based Views)

#ejemplo
def index(request):
    titulo = "soy un título"
    subtitulo = "soy un subtítulo"
    return render(request, 'post/post.html',{
        "titulo":titulo,
        "subtitulo":subtitulo,
    })
    
def categorias(request):
    return render(request, 'categorias.html')
    
    
    
    
    
  
    
        
    
