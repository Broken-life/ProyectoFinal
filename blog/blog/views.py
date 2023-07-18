from django.shortcuts import render, HttpResponse
from django.urls import reverse
from django.template import loader
from apps.post.models import Categoria, User


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

def about(request):
    nosotros = "esto es un grupo del informatorio formado en el año 2023"
    return render(request, "about.html",{
        "nosotros":nosotros,
    })