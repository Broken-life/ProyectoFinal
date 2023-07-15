from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"), #pagina principal
    path("login/", include("apps.login.urls")), #apartado de login
    path("post/", include("apps.post.urls")), #apartado de post
]