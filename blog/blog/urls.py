from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"), #pagina principal
    path("login/", include("apps.login.urls")), #apartado de login
    path("post/", include("apps.post.urls")), #apartado de post
    #path("crear-articulo/", include("apps.post.urls")),
    #path('home/', views.home, name="home"),
    path("about/", views.about, name="acerca"),
    path('contact/',views.contacto, name="contacto"),
    #path('categorias/', views.publicaciones, name="categorias"),
    path('crear-categoria/', views.crear_categoria, name="nueva categoria"),
    #path('detalle_publicacion/', views.detalle_publicacion, name="detalle_publicacion"),
    path('crear_post/', views.agregar_publicacion, name='crear_post'),
    path('editar_post/<int:id>/', views.editar_publicacion, name='editar_post'),
    path('eliminar_post/<int:id>/', views.eliminar_publicacion, name='eliminar_post'),
    #path('categorias/', views.mostrar_articulo, name="mostrar_articulo"),
    #path('crear_comentario/<int:post_id>/', views.crear_comentario, name='crear_comentario'),
    path('mostrar-comentario/', views.mostrar_comentarios, name="mostrar"),
]