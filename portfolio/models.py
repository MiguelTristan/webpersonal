from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripción')

    # el 'upload_to' es para tener organizada la media creando un fichero 'projects' y ahi almacenando los archivos
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'projects')

    # el atributo 'auto_now_add' se ejecuta cuando se crea por 1ra vez el registro
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación')

    # el atributo 'auto_now' se ejecuta solo cuando se actualiza el registro
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de actualización')

    url_link = models.URLField(null = True, blank = True, verbose_name = 'URL')

    # la clase 'Meta' para definir metadatos en el sitio admin
    class Meta:
        # verbose_name -establezco titulos publicos para el sitio admin
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        # el orden es el del nuevo al antiguo solo con poner el '-'
        ordering = ['-created']

    # metodo especial para obtener el titulo del proyecto y 'self' indico una clase normal
    def __str__(self):
        return self.title
