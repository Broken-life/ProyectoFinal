from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


def categorias(request):
   
    return render(request, "category.html")

def contacto(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")