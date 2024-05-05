from datetime import datetime, timedelta

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StreetLeader(TimestampedModel):

    name = models.CharField('Nombre', max_length=20)
    last_name = models.CharField('Apellido', max_length=20)
    street = models.TextField('Calle')
    phone = models.CharField('Telefono', max_length=20, unique=True)
    email = models.EmailField('Correo', unique=True)
    photo = models.ImageField('Foto', upload_to='foto')
    facebook = models.URLField('Facebook')

    class Meta:
        verbose_name = 'Lider de calle'
        verbose_name_plural = 'Lideres de calle'

    def __str__(self):
        return f'{self.name} {self.last_name}'
    


class News(TimestampedModel):

    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField('Foto', upload_to='foto')
    slug = models.SlugField(editable=False, max_length=300)
  

    class Meta:
        verbose_name = 'Noticia'
        verbose_name_plural = 'Noticias'

    def __str__(self):
        return self.title
    
     #Generar slug unico
    
    def save(self, *args, **kwargs):
        now =  datetime.now()
        totaltime = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(totaltime.total_seconds())
        slug_unique = f'{self.title}{str(seconds)}'
        self.slug = slugify(slug_unique)
        super(News, self).save(*args, **kwargs)


class Contact(TimestampedModel):
    name = models.CharField('Nombre', max_length=10)
    last_name = models.CharField('Apellido', max_length=20)
    email = models.EmailField('Correo')
    phone = models.CharField('Telefono', max_length=20)
    street = models.TextField('Calle o Direccion', max_length=255)
    message = models.TextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
    
    def __str__(self):
        return f'{self.name} {self.last_name} | {self.street}'
    
class Attachment(TimestampedModel):
    title = models.CharField('Titulo', max_length=200)
    description = models.TextField('Descripcion')
    date = models.DateField('Fecha de Jornada', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField('Foto', upload_to='foto')
    slug = models.SlugField(editable=False, max_length=300)
  

    class Meta:
        verbose_name = 'Nueva Jornada'
        verbose_name_plural = 'Nuevas Jornadas'

    def __str__(self):
        return self.title
    
     #Generar slug unico
    
    def save(self, *args, **kwargs):
        now =  datetime.now()
        totaltime = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(totaltime.total_seconds())
        slug_unique = f'{self.title}{str(seconds)}'
        self.slug = slugify(slug_unique)
        super(Attachment, self).save(*args, **kwargs)
