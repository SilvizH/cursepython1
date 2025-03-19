from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    resumo = models.CharField(max_length=300)
    conteudo = RichTextField()
    imagem = models.ImageField(upload_to='posts/')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
