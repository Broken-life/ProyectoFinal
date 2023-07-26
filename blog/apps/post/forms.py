from django import forms
from .models import Comentario, Post

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 4}),  # Para darle un tamaño adecuado al campo de contenido
        }

class FormularioArticulo(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'resumen', 'imagen', 'categoria', 'permitir_comentarios']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 8}),  # Para darle un tamaño adecuado al campo de contenido
        }
        
class CrearArticuloForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
