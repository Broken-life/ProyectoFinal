from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Comentario, User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria
#from apps.post.forms import publicacionForm


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


#@login_required(login_url='/categorias/')
def ver_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentario_set.all()
    
    
    # Pasar la lista de comentarios al contexto
    context = {
        'publicacion': post,
        'comentarios': comentarios,
    }

    return render(request, 'category.html', context)

def publicaciones(request):
    posteo = Post.objects.count()
    publicaciones = Post.objects.all()
    comentarios = Comentario.objects.all()
    return render(request, 'category.html',{
        'posteo':posteo, 
        'publicaciones':publicaciones,
        'comentarios':comentarios,
        })
    

def agregar_publicacion(request):
    if request.method == 'POST':
        formPost = publicacionForm(request.POST)
        if formPost.is_valid():
            formPost.save()
            return render ('category.html')
            
    else:
          formPost = publicacionForm()
          
         
        
    return render(request, 'nueva_publicacion.html',{'formPost':formPost})
        
# acá termina el código      

#@login_required   
#este código funciona     
def editar_publicacion(request, id):
    publicacion = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        formPost = publicacionForm(request.POST, instance=publicacion)
        if formPost.is_valid():
            formPost.save()
            return redirect('categorias')
            
    else:
        
        formPost = publicacionForm(instance=publicacion)
          
         
        
    return render(request, 'editar.html',{'formPost':formPost})

# acá termina el código  

#@login_required   
#este código funciona   
def eliminar_publicacion(request, id):
    publicacion = get_object_or_404(Post, pk=id)
    if publicacion:
        publicacion.delete()
    return redirect('categorias')

# acá termina el código          
    
    
    
    
    
  
    
        
    
