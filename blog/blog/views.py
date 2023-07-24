from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.template import loader
from apps.post.models import Categoria, User, Comentario, Post
from .forms import CrearArticuloForm
from django.forms import modelform_factory
from django.contrib.auth.decorators import login_required
from datetime import date
#from .forms import publicacionForm

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def categorias(request):
    posteo = Post.objects.count()
    publicaciones = Post.objects.all()
    return render(request, 'category.html', {'posteo':posteo, 'publicaciones':publicaciones})

  

def contacto(request):
    contacto = "3731-498413"
    return render(request, "contact.html",{
        "contacto":contacto,
    })



def about(request):
    usuarios = User.objects.all()
    correos = User.objects.all()
    return render(request, "about.html",{
        "usuarios":usuarios,
        "correos":correos,
    })
    
def crear_categoria(request):
    try:
        cat = Categoria.objects.get(pk=41)
        response = f"<h2>categoria nueva: {cat.titulo}</h2>"
    except:
        response = "Categoria no encontrada"
    return HttpResponse(response)



def detalle_publicacion(request):
    publicacion = Post.objects.all()
    return render(request, 'detalle_public.html',{'publicacion':publicacion})

# agregamos una publicacion

publicacionForm = modelform_factory(Post, exclude=['imagen','fecha_actualizacion'])

#@login_required   
#este código funciona    
def agregar_publicacion(request):
    if request.method == 'POST':
        formPost = publicacionForm(request.POST)
        if formPost.is_valid():
            formPost.save()
            return redirect('categorias')
            
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



# def post_detail(request, id):
#     post = get_object_or_404(Post, pk=id)

#     if request.method == 'POST':
#         formComentario = ComentarioForm(request.POST)
#         if formComentario.is_valid():
#             comentario = formComentario.save(commit=False)
#             comentario.post = post
#             comentario.autor = request.user  # Assuming you're using authentication
#             comentario.save()
#             return redirect('post_detail', id=id)

#     else:
#         formComentario = ComentarioForm()

#     return render(request, 'post_detail.html', {'post': post, 'formComentario': formComentario})  

#@login_required(login_url='/categorias')

# def crear_comentario(request, post_id):
#     if request.method == 'POST':
#         contenido = request.POST.get('contenido')
#         autor = request.user
#         post = Post.objects.get(id=post_id)
#         fecha_creacion = date.today()  # Obtiene la fecha actual
#         comentario = Comentario(contenido=contenido, autor=autor, post=post, fecha_creacion=fecha_creacion)
#         comentario.save()

#     # Obtiene todos los comentarios asociados al post
#     comentarios = Comentario.objects.filter(post=post)

#     # Obtiene la publicación para mostrarla en la plantilla
#     publicacion = Post.objects.get(id=post_id)
  
#     return render(request, 'category.html', {'publicacion': publicacion, 'comentarios': comentarios})

@login_required(login_url='/categorias/')
def crear_comentario(request, post_id):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        autor = request.user
        post = Post.objects.get(id=post_id)
        Comentario.objects.create(contenido=contenido, autor=autor, post=post)

    return redirect('categorias')

    
 
def mostrar_comentarios(request):
    contenido = Comentario.objects.all()
    print(contenido)  # Agregar esta línea para ver los comentarios en la consola
    context = {
        "contenido": contenido,
    }
    return render(request, 'category.html', context)
  

    


    
  
          
         
        


 
    
    