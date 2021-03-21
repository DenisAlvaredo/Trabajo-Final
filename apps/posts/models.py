from django.db import models
from django.conf import settings
from django.utils import timezone
from django.conf import settings
from django.urls import reverse 
from apps.users.models import User
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre = models.CharField('Categoría', max_length = 50, null = False, blank = False)
    estado = models.BooleanField('Categoría activa/Categoría no activa', default = True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now = False, auto_now_add = True) #auto_now = False es para que no modifique su fecha si se llega a actualizar

    class Meta: 
        verbose_name = 'Categoría' #los verbose name, es para que se utilice un nombre si solo existe una y el otro si hay mas de una categoria
        verbose_name_plural = 'Categorías'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre or ''



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField('Título del post', max_length = 100, null = False, blank = False)
    categoria = models.CharField(max_length = 255, default='elegir categoria')
    contenido = RichTextField()
    miniatura = models.ImageField('Portada')
    slug = models.SlugField('Slug', max_length = 100, blank = False, null = False)
    fecha_publicacion = models.DateTimeField('Fecha de publicación', default = timezone.now) 
    ultima_actualizacion = models.DateTimeField('Última actualización', auto_now = True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo or ''

    def __str__(self):
        return self.contenido or ''

    def __str__(self):
        return self.author or ''

    def __str__(self):
        return self.categoria or ''
        

class Comentarios(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name="comentarios", on_delete=models.CASCADE)
    # Se asocia la clase Comment con la clase Post y si se borra post se borra el comment
    comentario = RichTextField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.titulo, self.post.author)  or ''