from django import forms
from apps.post.models import Post

class CrearArticuloForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
       


        