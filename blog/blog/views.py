from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.template import loader
from apps.post.models import Categoria, User, Comentario


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def categorias(request):
    titulo = Categoria.objects.all()
    
    template = loader.get_template('category.html')
    context = {
        "titulo":titulo,
       
    }
 
    return HttpResponse(template.render(context, request))
    
   


def contacto(request):
    contacto = "3731-498412"
    return render(request, "contact.html",{
        "contacto":contacto,
    })

# def about(request):
#     nosotros = "esto es un grupo del informatorio formado en el año 2023"
#     return render(request, "about.html",{
#         "nosotros":nosotros,
#     })

def about(request):
    usuarios = User.objects.all()
    correos = User.objects.all()
    return render(request, "about.html",{
        "usuarios":usuarios,
        "correos":correos,
    })
    
# def crear_categoria(request):
#     try:
#         cat = Categoria.objects.get(pk=41)
#         response = f"<h2>categoria nueva: {cat.titulo}</h2>"
#     except:
#         response = "Categoria no encontrada"
#     return HttpResponse(response)

# def mostrar_comentario(request):
#     com = Comentario.objects.all()
    
#     return HttpResponse(f"<h2>nuevo comentario: {com.contenido} fecha de creación: - {com.fecha_creacion} fecha de actualizacion: {com.fecha_actualizacion}</h2>")

def mostrar_comentario(request):
    contenido = Comentario.objects.all()
    fecha_creacion = Comentario.objects.all()
    return render(request, "about.html",{
        "contenido":contenido,
        "fecha_creacion":fecha_creacion,
    })

   