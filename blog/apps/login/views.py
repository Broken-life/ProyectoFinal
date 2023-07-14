from django.shortcuts import render
# Aca van las vistas de la app login (Basic Views - Function Based Views)

#ejemplo
def index(request):
    return render(request, 'login/index.html')