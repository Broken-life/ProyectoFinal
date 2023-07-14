from django.shortcuts import render

# Aca van las vistas de la app post (Basic Views - Function Based Views)

#ejemplo
def index(request):
    return render(request, 'post/index.html')

