from django.urls import path, include
from . import views  # importamos las vistas de la app post

# Aca van las urls de la app post

app_name = "post" # le damos un nombre a la app para evitar hardcodear en los templates
urlpatterns = [
    path("", views.index, name="index"), 
    path('ver_post/<int:post_id>/', views.ver_post, name='ver_post'),
    path('publicaciones/', views.publicaciones, name="publicaciones"),
    path('crear_post/', views.agregar_publicacion, name='crear_post'),
    path('editar_post/<int:id>/', views.editar_publicacion, name='editar_post'),
    path('eliminar_post/<int:id>/', views.eliminar_publicacion, name='eliminar_post'),
    #path("crear-articulo/", views.crear_articulo),
    #path('post/',views.new_post_view, name='new-post'),
    # es porque la vista es una function based view
    #path("post/", views.PostView.as_view(), name="post"),  # es porque la vista es una basic view
]