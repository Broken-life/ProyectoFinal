from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Categoria, User, Comentario
#from apps.post.forms import publicacionForm ##donde esta publicacionForm??? D:
from django.forms import modelform_factory
from django.core.paginator import Paginator
from datetime import date



    
def categorias(request):
    return render(request, 'categorias.html')


def ver_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comentarios = post.comentario_set.all()#trae todos los comentarios de este post en particular
    context = {
        'publicacion': post,
        'comentarios': comentarios,
    }
    return render(request, 'post/post_detail.html', context)#crear html de post

#USAR PAGINADO CON PAGINATOR
def post_list(request):
    cant_posts = Post.objects.count()
    post = Post.objects.all()
    comentarios = Comentario.objects.all()
    return render(request, 'post/post_list.html',{
        'cant_posts':cant_posts, 
        'post':post,
        'comentarios':comentarios,
        })
    

def crear_post(request):
    publicacionForm = modelform_factory(Post, exclude=['fecha_actualizacion'])
    if request.method == 'POST':
        formPost = publicacionForm(request.POST)
        if formPost.is_valid():
            formPost.save()
            print(formPost.instance.id)
            #return redirect ('ver_post', formPost.instance.id)         
    else:
        formPost = publicacionForm()   
    return render(request, 'post/new_post.html',{'formPost':formPost})



def editar_post(request, id):
    publicacionForm = modelform_factory(Post, exclude=['imagen','fecha_actualizacion'])
    publicacion = get_object_or_404(Post, pk=id)
    formPost = publicacionForm(request.POST, instance=publicacion)
    if request.method == 'POST':
        if formPost.is_valid():
            formPost.save()
            return redirect('ver_post', publicacion.id)  
        
    return render(request, 'post/update_post.html',{'formPost':formPost})


def eliminar_post(request, id):
    publicacion = get_object_or_404(Post, pk=id)
    if (request.user == publicacion.autor ):
        if request.method == 'POST':
            publicacion.delete()
            return redirect('publicaciones')
    else:
        return redirect('index')     
    return render(request, 'post/delete_post.html',{'publicacion':publicacion})


