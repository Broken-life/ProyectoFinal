from django.urls import path, include
from . import views  # importamos las vistas de la app post

# Aca van las urls de la app post

app_name = "post" # le damos un nombre a la app para evitar hardcodear en los templates
urlpatterns = [
    path("", views.index, name="index"), 
    #path("crear-articulo/", views.crear_articulo),
   
  
   
    #path('post/',views.new_post_view, name='new-post'),
    # es porque la vista es una function based view
    #path("post/", views.PostView.as_view(), name="post"),  # es porque la vista es una basic view
]