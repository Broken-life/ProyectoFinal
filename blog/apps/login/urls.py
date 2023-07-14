from django.urls import path
from . import views  # importamos las vistas de la app login

# Aca van las urls de la app login

app_name = "login" # le damos un nombre a la app para evitar hardcodear en los templates
urlpatterns = [
    path("", views.index, name="index"),  # es porque la vista es una function based view
    #path("logout/", views.LogoutView.as_view(), name="logout"),  # es porque la vista es una basic view
]