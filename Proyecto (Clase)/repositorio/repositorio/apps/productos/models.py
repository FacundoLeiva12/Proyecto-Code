from django.db import models
from django.utils import timezone

# Create your models here.



#Categorias
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo= models.CharField(max_length=50, null=False)
    subtitulo= models.CharField(max_length=100, null=False, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(defaul=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True,default='Sin categoria')
    imagen= models.ImageField(null=True, Blank=True, upload_to='media', default='static/post_defaul.png')
    publicado = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-publicado',)
        
        def __str__(self):
            return self.titulo
        
        def delete(self, using =None , keep_parents =False):
            self.imagen.delete(self.imagen.name)
            super().delete()