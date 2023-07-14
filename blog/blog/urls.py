from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")), #inicio de la pagina
    path("login/", include("apps.login.urls")), #apartado de login
    path("post/", include("apps.post.urls")), #apartado de post
]