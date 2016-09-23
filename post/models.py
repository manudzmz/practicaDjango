from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(User)
    titulo = models.CharField(max_length=150)
    intro = models.CharField(max_length=150)
    cuerpo = models.TextField()
    url = models.URLField()
    fec_publicacion = models.DateTimeField("fecha de publicación")

    def __str__(self):  # mipost.__str__()
        return self.titulo
