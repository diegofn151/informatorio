from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    decripcion = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=120)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    autor = models.CharField(max_length=50, null=True, blank=True)
    imagen = models.ImageField(upload_to = 'noticias',null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.CharField(max_length=50, null=False, blank=False)
    creado = models.DateField(auto_now_add=True)
    cuerpo = models.TextField()
    titulo = models.ForeignKey(Noticia, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.cuerpo