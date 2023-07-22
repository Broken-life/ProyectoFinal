from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.urls import reverse
from django.template import loader
from apps.post.models import Categoria, User, Comentario, Post
from .forms import CrearArticuloForm
from django.forms import modelform_factory


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
            
  
          
         
        


 
    
    