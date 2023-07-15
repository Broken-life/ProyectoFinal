from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', include("apps.login.urls")),
    path('post/', include("apps.post.urls")),
]