from post.models import Post
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['owner']
